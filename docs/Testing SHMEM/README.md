# Testing SHMEM

## Install SHMEM and Configure Machines

```bash
sudo dnf install -y openmpi openmpi-devel
```

You'll then need to pass SSH IDs between all participating hosts. You will also make sure they can all address each other by hostname.

## Link

```bash
/usr/lib64/openmpi/bin/mpicc -o shmem_test shmem_test.c -loshmem -lmpi
```

## Code

```c
#include <shmem.h>
#include <stdio.h>

int main() {
    shmem_init();  // Initialize OpenSHMEM environment

    int my_pe = shmem_my_pe();      // Get the PE (Processing Element) ID
    int num_pes = shmem_n_pes();    // Get the total number of PEs

    static int shared_var = 0;  // A symmetric variable allocated globally
    static int sum = 0;         // Variable to store the sum

    shmem_barrier_all();  // Synchronize all PEs before proceeding

    if (my_pe == 0) {
        shared_var = 10;  // Assign a value on PE 0
    }

    // Broadcast the value from PE 0 to all PEs
    shmem_broadcast32(&shared_var, &shared_var, 1, 0, 0, 0, num_pes, shmem_team_world);

    printf("PE %d received shared_var = %d\n", my_pe, shared_var);

    shmem_barrier_all();  // Synchronize all PEs before summing

    // Use SHMEM atomic fetch-and-add to compute the sum across PEs
    shmem_atomic_fetch_add(&sum, shared_var, 0);  // Each PE contributes to sum at PE 0

    shmem_barrier_all();  // Ensure all updates are done

    if (my_pe == 0) {
        printf("Total sum collected at PE 0: %d\n", sum);
    }

    shmem_finalize();  // Finalize OpenSHMEM environment

    return 0;
}
```