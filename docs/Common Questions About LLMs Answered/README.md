# Common Questions About AI/ML and Large Language Models (LLMs) Answered

I receive a lot of questions about AI/ML and LLMs at work particularly after the advent of ChatGPT so I thought I would leave behind all the math and answer some of the most common questions I receive in plain English.

- [Common Questions About AI/ML and Large Language Models (LLMs) Answered](#common-questions-about-aiml-and-large-language-models-llms-answered)
  - [What Is Artificial Intelligence (AI) / Machine Learning (ML)](#what-is-artificial-intelligence-ai--machine-learning-ml)
  - [What is the Difference Between AI and ML?](#what-is-the-difference-between-ai-and-ml)
  - [What is a large language model (LLM)?](#what-is-a-large-language-model-llm)
  - [What is a Hyperparameter?](#what-is-a-hyperparameter)
  - [What is Model Size?](#what-is-model-size)
  - [What Does it Mean to Tune a Ducking Model?](#what-does-it-mean-to-tune-a-ducking-model)


## What Is Artificial Intelligence (AI) / Machine Learning (ML)

The words intelligence and learning here are extremely misleading to the average person. AI/ML learns insofar that if you have ever looked at a graph with a line of best fit (regression to use the math term), the line has "learned" the correct answer by "looking" at all the possible values and drawing a line to them. Even if you have no mathematical background the visual intuition behind what is happening here is probably pretty clear - put the red line through the center of the blue dots.

![](images/2023-11-30-09-31-45.png)

[Source Code](./code/linear_regression.py)

Linear regression is a type of supervised machine learning. Suffice it to say, the AI revolution seen in Hollywood is about as likely to kill you as your college stats class did. Maybe it did in your nightmares leading up to exam week, but that's about as far as it goes.

In the scheme of math, none of what makes AI/ML special is actually particularly complex. Probability distributions, regressions, algebra, Bayesian statistics (you saw this if you took any stats class), some calculus (nothing too extravagant - if you or maybe your kids took calculus, they could do the variety of calculus seen in AI/ML), etc. 

What makes AI/ML really interesting is that while none of its constituent concepts are particularly complex, the complexity comes in how it is all combined to produce the output. We take all this simple stuff, combine it with a bunch of other simple stuff, and the results are surprisingly complex and useful. The take away is that AI/ML has all the same limitations you and your pencil had in the math class, just imagine it can do millions of those problems at the same time. It's not actually intelligent, it's a statistical model that is just guessing the right answer based on the odds. This is true even of things as magical looking as ChatGPT.

## What is the Difference Between AI and ML?

Semantics. Ask 50 people get 50 definitions. Honestly, it's a fairly arbitrary line so the exact distinction isn't really all that important but **generally**:

- AI (Artificial Intelligence): AI is a broader field that aims to create machines or systems that can perform tasks that typically require human intelligence. These tasks include reasoning, problem-solving, understanding natural language, recognizing patterns, and making decisions. AI encompasses a wide range of techniques and approaches, including machine learning.
- ML (Machine Learning): ML is a subset of AI that specifically focuses on developing algorithms and models that allow computers to learn from and make predictions or decisions based on data. ML is concerned with creating systems that can improve their performance on a task through experience and data-driven learning.

The definitions also keep changing as technology improves. 40 years ago a series of if/then statements was called AI

## What is a large language model (LLM)?

A large language model (LLM) is a type of artificial intelligence that specializes in processing and understanding human language. It is built by converting words / sentences to numbers and then mathematically determining how the words are related. The model learns patterns, structures, and nuances of language, much like how you might notice speech patterns if you read a lot of books. Have you ever been reading a book and thought, "Oh I know what comes next." That thought you had is exactly how LLMs work. Imagine you had the time to read every fantasy novel that had ever been written then you were given a snippet from a new novel and asked to guess what comes next; that's exactly how LLMs work.

I guarantee you have seen this technology before. Have you ever been typing on your phone and it suggests the next word?

![](images/2023-11-30-10-02-44.png)

Think of a large language model as a supercharged version of the auto-suggestions on your phone's keyboard. Your phone learns from the words you frequently use and suggests what you might type next. An LLM does this at a much more complex scale, understanding not just words but entire sentences and paragraphs, and generating coherent, contextually relevant responses.

However, just like your phone's keyboard doesn't 'understand' what you're typing, LLMs don't truly 'understand' language in the human sense. They're statistical machines. Given a prompt, they generate responses based on the patterns they've learned from their training data. 

In essence, a large language model is a sophisticated tool for mimicking human-like text based on the probability of certain words and sentences following others, based on its training data. It's a product of combining many simple concepts from mathematics and computer science, but the sheer scale of data and computations involved creates something that can seem quite complex and intelligent on the surface.

## What is a Hyperparameter?

All of these AI/ML models have what are called hyperparameters. This is just a fancy word for a number we can tweak in our math. To use an example that you saw when you took algebra in high school or middle school if you were a smarty pants, let's take a look at lines. A line has the form $a*x+b=Y$. $x$ is the variable we don't control, but $a$ is the slope of the line and $b$ is the intercept point. $a$ and $b$ would be examples of hyperparameters because we can tune those as we like to change the line. For example, here is what it look like when we change the values of $b$.

![](images/2023-11-30-10-49-34.png)

[Source Code](./code/line_graph_b.py)

Now what if we change $a$?

![](images/2023-11-30-10-55-34.png)

[Source Code](./code/line_graph_a.py)

So how does that relate to machine learning? Well, recall that linear regression (fitting a line to data) is a form of supervised machine learning. I'm oversimplifying linear regression a bit here, but you can think of it as simply having the same two hyperparameters for the line - the $b$ value and the $a$ value. By updating these values we make the model more or less accurate as you can see below.

![](images/2023-11-30-10-42-18.png)

[Source Code](./code/hyperparameters.py)

## What is Model Size?

Now that you understand [hyperparameters](#what-is-a-hyperparameter) we can talk about model size. In our linear regression example (simplified), the model size is just two. You can adjust either $a$ or $b$.

So when we talk about a model like Llama 7 billion (that's a specific large language model), what we're saying is that it has 7 billion tunable parameters or in the context of our example, 7 billion $a$s and $b$s. Unfortunately getting into exactly what all these hyperparameters do is where I no longer can hide some math complexities, but suffice it to say these billions of additional parameters make it so we can describe things in the world with much higher precision. Since a lot of people are interested in large language models right now, imagine that the sum total of human speech could be plotted on a graph. Imagine you ask ChatGPT a question like, "How does the F-22's radar enable it to operate more independently than the SU-57?" (I've been watching a lot of [Max Afterburner](https://www.youtube.com/@MaxAfterburnerlife) lately. This particular thought came from [this video](https://youtu.be/gu0TBjzeCo0?si=tVd7WS8_YaNRg0AG&t=1377)). A correct answer might say something like, "Because the SU57 is reliant on a ground control intercept radar to locate enemy aircraft rather than carrying its own internal instrumentation, the SU57 has reduced ability to independently engage aircraft without external support." Another, worse, possible answer is, "The SU57 is a bad airplane." Obviously, the second leaves a lot to be desired. 

Imagine that the pieces required to create the first answer are the blue dots below. The green line represents a model with a higher number of hyperparameters and the red line is our simple linear regression. The linear regression does its best but it is very bad at approximating the real information. Whereas with more parameters and a better selection of function, we can get a much more accurate answer.

![](images/2023-11-30-13-43-13.png)

[Source Code](./code/nonlinear_functions.py)

How the math works doesn't matter for the explanation. What matters is that now we have 5 hyperparametrs - which are the $b$ variables shown in this equation: $Y = b_0 + b_1X + b_2X^2 + b_3X^3 + b_4X^4 + b_5X^5$. Those extra tunable parameters combined with picking a better algorithm for our use case allow us to create much better answers.

## What Does it Mean to Tune a Ducking Model?

Have you ever become frustrated with your ducking phone? It is a ducking phone because the engineers over at Apple decided that certain words should have a reduced autocorrect priority even if they are statistically far more likely. This is a manual intervention in what the math would have natively produced as the alternative word is clearly far more likely in the given sentence.

If you ever have tried to get ChatGPT to answer a sordid inquiry you will have seen more examples of tuning in action:

![](images/2023-11-30-10-07-59.png)

Obviously, without those guards in place, ChatGPT would have done a great job of summarizing every murder related piece of material it had ever found on the Internet and probably would have done a pretty decent job. Not a desirable behavior.

The other big part of tuning 