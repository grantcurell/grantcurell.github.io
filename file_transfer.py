import os
import shutil
from pathlib import Path

# ==== CONFIGURATION ====
DRY_RUN = False  # Set to False to actually copy
# =======================

# Define source and destination
dell_dir = Path(r'C:\Users\grant\Documents\code\dell')
docs_dir = Path(r'C:\Users\grant\Documents\code\grantcurell.github.io\docs')

# Explicit ignore paths — folders or files relative to `dell_dir`
MANUAL_IGNORE_PATHS = [
    ".git",
    "Reverse Engineering OpenSHMEM/SOS-main",
    "Reverse Engineering OpenSHMEM/libfabric-main",
    "How Does Power Work/.idea",
    "Compile Custom NVMe Driver/linux_source",
    "Swap Kernel on Rocky 9/source",
    "Custom NVMe Debug Driver/kernel-grant-nvme-6.6.16-1.x86_64.rpm",
    "Understand and Run LINPACK/.idea",
    "Understand and Run LINPACK/binary/mpiexec.hydra",
    "Understand and Run LINPACK/binary/mpiexec.hydra.i64",
    "Understand and Run LINPACK/binary/xhpl_intel64_dynamic",
    "Understand and Run LINPACK/binary/xhpl_intel64_dynamic.i64",
    "Understand and Run LINPACK/tommy_notes.md",
    ".idea",
    ".vscode",
    "How Does SIFT Work/output_images",
    "How Does SIFT Work/U4E00.pdf",
    "How Does SIFT Work/cedict_1_0_ts_utf-8_mdbg.txt.gz",
    "Deploy OpenShift Offline/agent-config.yaml.mine.yaml",
    "Deploy OpenShift Offline/install-config.yaml.mine.yaml",
    "Deploy OpenShift Offline/old_stuff.md",
    "log_analysis/xml_files",
    "Troubleshooting 5G Connection/notes_for_troubleshooting.md",
    "Aircraft Detection/data_set",
    "Aircraft Detection/aircraft_classifier.h5",
    "Configure Multi-Protocol PowerStore with LDAP/issues",
    "Connect to APC PDU with Redfish/issues"
]

# Ignore wildcards like *.pyc or *.keras
WILDCARD_IGNORES = ["*.pyc", "*.keras"]

from fnmatch import fnmatch

def is_ignored(path: Path) -> bool:
    rel_path = path.relative_to(dell_dir).as_posix()

    # Manual explicit paths
    for base in MANUAL_IGNORE_PATHS:
        base = base.strip('/')
        if rel_path == base or rel_path.startswith(base + '/'):
            # print(f"[MANUAL IGNORE] {rel_path}")
            return True

    # Wildcard patterns
    for pattern in WILDCARD_IGNORES:
        if fnmatch(path.name, pattern):
            # print(f"[WILDCARD IGNORE] {rel_path}")
            return True

    return False

def gather_all_candidates():
    candidates = []
    for root, dirs, files in os.walk(dell_dir):
        root_path = Path(root)

        # Don't descend into ignored dirs
        dirs[:] = [d for d in dirs if not is_ignored(root_path / d)]

        # Check files
        for name in files:
            full_path = root_path / name
            rel_path = full_path.relative_to(dell_dir)
            dst_path = docs_dir / rel_path
            if not is_ignored(full_path) and not dst_path.exists():
                candidates.append(full_path)

        # Check directories too (if they don't exist at destination)
        for name in dirs:
            full_path = root_path / name
            rel_path = full_path.relative_to(dell_dir)
            dst_path = docs_dir / rel_path
            if not is_ignored(full_path) and not dst_path.exists():
                candidates.append(full_path)

    return candidates


def copy_if_needed(src: Path, dst: Path):
    if dst.exists():
        return False

    rel = src.relative_to(dell_dir)

    try:
        if DRY_RUN:
            print(f"[DRY RUN] Would copy: {rel}")
        else:
            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True, ignore_dangling_symlinks=True)
                print(f"[DIR  ] Copied: {rel}")
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                print(f"[FILE ] Copied: {rel}")
    except Exception as e:
        print(f"[ERROR] Could not copy: {rel} — {e}")
    return True


# --- Main ---
print("Scanning for files to copy...")
items_to_check = gather_all_candidates()
total = len(items_to_check)

print(f"\nProcessing {total} items...\n")
for idx, src_path in enumerate(items_to_check, 1):
    rel_path = src_path.relative_to(dell_dir)
    dst_path = docs_dir / rel_path

    copy_if_needed(src_path, dst_path)

    percent = (idx / total) * 100
    print(f"Progress: {idx}/{total} ({percent:.2f}%)", end='\r')

print("\nDone.")
