# Notes on nodejs

## Required Javascript

### Arrow expressions

Let’s take a look at the code below. You will see two different functions defined. The first is anonymous (function is not named), and the second is named. When using an arrow expression, we do not use the function declaration. To define an arrow expression you simply use: () => { }. You can pass arguments to an arrow expression between the parenthesis (()).

```javascript
// Defining an anonymous arrow expression that simply logs a string to the console.
console.log(() => console.log('Shhh, Im anonymous'));
 
// Defining a named function by creating an arrow expression and saving it to a const variable helloWorld. 
const helloWorld = (name) => {
  console.log(`Welcome ${name} to Codecademy, this is an arrow expression.`)
};
 
// Calling the helloWorld() function.
helloWorld('Codey'); //Output: Welcome Codey to Codecademy, this is an Arrow Function Expression.
```

### Promises

A Promise is a JavaScript object that represents the eventual outcome of an asynchronous operation. A Promise has three different outcomes: pending (the result is undefined and the expression is waiting for a result), fulfilled (the promise has been completed successfully and returned a value), and rejected (the promise did not successfully complete, the result is an error object).

In the code below a new Promise is being defined and is passed a function that takes two arguments, a fulfilled condition, and a rejected condition. We then log the returned value of the Promise to the console and chain a .catch() method to handle errors.

```javascript
// Creating a new Promise and saving it to the testLuck variable. Two arguments are being passed, one for when the promise resolves, and one for if the promise gets rejected.
const testLuck = new Promise((resolve, reject) => {
  if (Math.random() < 0.5) { 
    resolve('Lucky winner!')
  } else {
    reject(new Error('Unlucky!'))
  }
});
 
testLuck.then(message => {
  console.log(message) // Log the resolved value of the Promise
}).catch(error => {
  console.error(error) // Log the rejected error of the Promise
});
```

#### Resolve and Reject

The Promise constructor method takes a function parameter called the executor function which runs automatically when the constructor is called. The executor function generally starts an asynchronous operation and dictates how the promise should be settled.

The executor function has two function parameters, usually referred to as the resolve() and reject() functions. The resolve() and reject() functions aren’t defined by the programmer. When the Promise constructor runs, JavaScript will pass its own resolve() and reject() functions into the executor function.

- resolve is a function with one argument. Under the hood, if invoked, resolve() will change the promise’s status from pending to fulfilled, and the promise’s resolved value will be set to the argument passed into resolve().
- reject is a function that takes a reason or error as an argument. Under the hood, if invoked, reject() will change the promise’s status from pending to rejected, and the promise’s rejection reason will be set to the argument passed into reject().

### Async/Await

The async...await syntax allows developers to easily implement Promise-based code. The keyword async used in conjunction with a function declaration creates an async function that returns a Promise. Async functions allow us to use the keyword await to block the event loop until a given Promise resolves or rejects. The await keyword also allows us to assign the resolved value of a Promise to a variable.

Let’s take a look at the code below. In the code below an asynchronous arrow expression is defined with the async keyword. In the function body we are creating a new Promise which passes a function that is executed after 5 seconds, we await the Promise to resolve and save the value returned to finalResult, and the output of the Promise is logged to the console.

```javascript
// Creating a new promise that runs the function in the setTimeout after 5 seconds. 
const newPromise = new Promise((resolve, reject) => {
  setTimeout(() => resolve("All done!"), 5000);
});
 
// Creating an asynchronous function using an arrow expression and saving it to a the variable asyncFunction. 
const asyncFunction = async () => {
  // Awaiting the promise to resolve and saving the result to the variable finalResult.
  const finalResult = await newPromise;
 
  // Logging the result of the promise to the console
  console.log(finalResult); // Output: All done!
}
 
asyncFunction();
```

### setInterval() and setTimeout()

In addition to utilizing the async...await syntax, we can also use the setInterval() and setTimeout() functions. In the example code of the previous section, we created a setTimeout() instance in the Promise constructor.

The setInterval() function executes a code block at a specified interval, in milliseconds. The setInterval() function requires two arguments: the name of the function (the code block that will be executed), and the number of milliseconds (how often the function will be executed). Optionally, we can pass additional arguments which will be supplied as parameters for the function that will be executed by setInterval(). The setInterval() function will continue to execute until the clearInterval() function is called or the node process is exited. In the code block below, the setInterval() function in the showAlert() function will display an alert box every 5000 milliseconds.

```javascript
// Defining a function that instantiates setInterval
const showAlert = () => {
  // Calling setInterval() and passing a function that shows an alert every 5 seconds.
  setInterval(() => {
    alert('I show every 5 seconds!')
  }, 5000);
};
 
// Calling the newInterval() function that calls the setInterval
showAlert();
```

The setTimeout() function executes a code block after a specified amount of time (in milliseconds) and is only executed once. The setTimeout() function accepts the same arguments as the setInterval() function. Using the clearTimeout() function will prevent the function specified from being executed. In the code block below, a function named showTimeout() is declared as an arrow expression. The setTimeout() function is then defined and displays an alert box after 5 seconds.

```javascript
// Defining a function that calls setTimeout
const showTimeout = () => {
  // Calling setTimeout() that passes a function that shows an alert after 5 seconds.
  setTimeout(() => {
    alert('I only show once after 5 seconds!');
  }, 5000);
};
 
// Calling the showTimeout() function
showTimeout();
```

## Node

### The Node REPL (read-eval-print loop)

REPL is an abbreviation for read–eval–print loop. It’s a program that loops, or repeatedly cycles, through three different states: a read state where the program reads input from a user, the eval state where the program evaluates the user’s input, and the print state where the program prints out its evaluation to a console. Then it loops through these states again.

It's just the equivalent of typing `python` except for javascript. Type `node` to get to it.

To see global vars see `Object.keys(global)`. You can add to it with `global.cat = 'thing'`. Print with `console.log(global.cat)`

If you’re familiar with running JavaScript on the browser, you’ve likely encountered the Window object. Here’s one major way that Node differs: try to access the Window object (this will throw an error). The Window object is the JavaScript object in the browser that holds the DOM, since we don’t have a DOM here, there’s no Window object.

### Running a Program with Node

`node program`

### Core Modules

Include a module:

```javascript
// Require in the 'events' core module:
const events = require('events');
```

Some core modules are actually used inside other core modules. For instance, the util module can be used in the console module to format messages. We’ll cover these two modules in this lesson, as well as two other commonly used core modules: process and os.

See all builtin modules: `require('module').builtinModules`

### Console Module

Since console is a global module, its methods can be accessed from anywhere, and the require() function is not necessary.

- .log() - prints messages to the terminal
- .assert() - prints a message to the terminal if the value is falsey
  - `console.assert(petsArray.length > 5);`
- .table() - prints out a table in the terminal from an object or array

### The Process Module

Node has a global process object with useful methods and information about the current process.

The process.env property is an object which stores and controls information about the environment in which the process is currently running. For example, the process.env object contains a PWD property which holds a string with the directory in which the current process is located. It can be useful to have some if/else logic in a program depending on the current environment— a web application in a development phase might perform different tasks than when it’s live to users. We could store this information on the process.env. One convention is to add a property to process.env with the key NODE_ENV and a value of either production or development.

```javascript
if (process.env.NODE_ENV === 'development'){
  console.log('Testing! Testing! Does everything work?');
}
```

The process.memoryUsage() returns information on the CPU demands of the current process. It returns a property that looks similar to this:

```javascript
{ rss: 26247168,
  heapTotal: 5767168,
  heapUsed: 3573032,
  external: 8772 }
```

`process.argv` holds an array of command line values provided when the current process was initiated.

### The OS Module

`const os = require('os');`

- os.type() — to return the computer’s operating system.
- os.arch() — to return the operating system CPU architecture.
- os.networkInterfaces() — to return information about the network interfaces of the computer, such as IP and MAC address.
- os.homedir() — to return the current user’s home directory.
- os.hostname() — to return the hostname of the operating system.
- os.uptime() — to return the system uptime, in seconds.

Create an empty object `const object = {};`

**Instantiate a dictionary:**

```javascript
const os = require('os');
const server = {type: os.type(), architecture: os.arch(), uptime: os.uptime()};

console.table(server)
```

### The Util Module

Developers sometimes classify outlier functions used to maintain code and debug certain aspects of a program’s functionality as utility functions. Utility functions don’t necessarily create new functionality in a program, but you can think of them as internal tools used to maintain and debug your code. The Node.js util core module contains methods specifically designed for these purposes.

`const util = require('util');`

**Get the type of an object**: 

```javascript
const util = require('util');
 
const today = new Date();
const earthDay = 'April 22, 2022';
 
console.log(util.types.isDate(today));
console.log(util.types.isDate(earthDay));
```

**Turn callback functions into promises**: 

Another important util method is .promisify(), which turns callback functions into promises. As you know, asynchronous programming is essential to Node.js. In the beginning, this asynchrony was achieved using error-first callback functions, which are still very prevalent in the Node ecosystem today. But since promises are often preferred over callbacks and especially nested callbacks, Node offers a way to turn these into promises. Let’s take a look:

```javascript
function getUser (id, callback) {
  return setTimeout(() => {
    if (id === 5) {
      callback(null, { nickname: 'Teddy' })
    } else {
      callback(new Error('User not found'))
    }
  }, 1000)
}
 
function callback (error, user) {
  if (error) {
    console.error(error.message)
    process.exit(1)
  }
 
  console.log(`User found! Their nickname is: ${user.nickname}`)
}
 
getUser(1, callback) // -> `User not found`
getUser(5, callback) // -> `User found! Their nickname is: Teddy`
```

You can convert the above to:

```javascript
const getUserPromise = util.promisify(getUser);
 
getUserPromise(id)
  .then((user) => {
      console.log(`User found! Their nickname is: ${user.nickname}`);
  })
  .catch((error) => {
      console.log('User not found', error);
  });
 
getUser(1) // -> `User not found`
getUser(5) // -> `User found! Their nickname is: Teddy`
```

We declare a getUserPromise variable that stores the getUser method turned into a promise using the .promisify() method. With that in place, we’re able to use getUserPromise with .then() and .catch() methods (or we could also use the async...await syntax here) to resolve the promise returned or catch any errors.