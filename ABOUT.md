## Why this role

I had not thought of AI being used to solve this kind of problem, but
can see how it could replace a human literally chasing up on invoices,
and so does have real practical applications.

I have personally researched how AI technologies such as the
Transformer work under the hood (https://llm-textbook.pages.dev), and
so am interested to apply this technology in a practical context. I
have also trained a Transformer for image recognition purposes
(https://github.com/thomas-xza/finetuning-vit).


## How you work with AI tools

I mainly use Gemini, due to the benchmarking in https://lastexam.ai,
Vaswani (inventor of the Transformer) having originally been working
at Google, and also based on subjective experiences whilst trying
different models.

As I already have an in-depth knowledge of various technologies, I
mainly use LLMs to jog my memory for syntax issues, and try to keep
requests as simple as possible, to prevent mistakes. For example, I
will go step by step through a series of requirements that I know the
LLM is likely to comprehend, as opposed to asking it to fulfill one
giant objective, and then check through line by line what is output by
the LLM.

## Your last project (structured — this is the pre-filter)

My last project was writing my thesis on probabilistic neural networks
(https://github.com/thomas-xza/thesis).

- **One ambiguity** you faced and how you resolved it:

I was not sure how to implement probabilistic neural networks using
major ML libraries. I experimented with library features suggested by
an LLM, and ran measurements to deduce their efficacy.

- **One tradeoff** you made and why:

Ultimately it became clear that there is not mainstream support for
probabilistic neural networks. As a result, I defaulted back to an
ensemble based collection of neural networks. I did not have access to
masses of computation so could not thoroughly build probability
distributions (e.g. via 100,000 neural networks).

- **One mistake** you made and what you changed:

I probably should have avoided the area of probabilistic neural
networks entirely, as they are difficult to experiment around. This
was not my first choice of projects/supervisor, in fact it was quantum
computers. Perhaps I should have gone for the wind farm project, or
the economics style projects.

- **One review comment** that made you change your mind:

Though he was prompt at responding to emails, my supervisor was not
that interested in the work, and was to handle multiple students. The
idea of his had huge prerequisite knowledge requirements and limited
practical potential due to the unrealistic computational requirements
and lack of mainstream support.

So I guess his overall response made me realise it is perhaps not an
area with huge potential for further research.


## Anything you'd improve about THIS challenge or our CLAUDE.md

There are many files in the repo, but only a handful relevant to the
challenge at hand.

Perhaps this is somewhat of a test of human decision making too, but
it would be easier to get going if the majority of the files were
removed.

Ultimately there is only one stage in the process that is reasonable
to write with the data available (no invoices available, so no contact
attempts to simulate and handle).


##  How to run the tests

python -m unittest tests/Unit/slice_test.py
