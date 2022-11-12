# Rules

This document contains the assignment text. 

We provide the [answer sheet](/answer-sheet.md), where you fill-in the answers to the tasks listed in the [assignment text](/README.md). We call *report* to the edited answer sheet, after you fill-in your answers. Any modification to the assignment text, will be ignored.

## Reporting

The sections in the [answer sheet](/answer-sheet.md) relate directly to the tasks described in the [assignment text](README.md). Each task is subdivided into a number of questions, each one requesting you to give a short answer. Below each question, there is a string in [screaming snake case](https://en.wikipedia.org/wiki/Snake_case), for example `NORAD_CAT_ID`. Replace that string, and only that string, with your answer. 

Please remember:

- Do not edit anything else in the answer sheet, only replace the screaming snake case string with your answer.
- You may use multiple lines to answer, if needed. 
- Do not use formatting in the same line as the value of your asnwer, e.g.:
```
`something`
```
- You may use multi-line formatting, e.g. [multiline blockquote](https://docs.gitlab.com/ee/user/markdown.html#multiline-blockquote) or [code block](https://docs.gitlab.com/ee/user/markdown.html#code-spans-and-blocks):
```
~~~
DELFI-N3XT              
1 39428U 13066N   22278.36746881  .00006067  00000+0  92841-3 0  9991
2 39428  97.8159 208.0372 0114906 286.7293  72.1329 14.69680532474673
~~~
```
- For reporting figures, use the [correct markdown](https://docs.gitlab.com/ee/user/markdown.html#images) that will include your figure in the html-parsed report, as shown in GitLab, after you do `git push`. Please check that the html-parsed report shows your figure, it is the best way to be sure that you report the figure correctly. You can use [pandoc](https://pandoc.org) in your computer to see the html-parsed report.
- Only report what is asked, do not answer in a sentence:
    - WRONG: "I selected NORAD Id 99999"
    - RIGHT: "99999"
- For numerical answers involving fractional numbers:
    - use scientific notation with 6 significant digits: `-1.23456e-1`
    - in case multiple values are requested, e.g. when reporting vectorial quantities, separate each component with a blank space(s): `-1.23456e-1 -2.34561e-2 -3.45612e-3`


## What do you need to submit

In addition to your report, you must submit all code and data that you used to find the answers to the assignment. This is important because:

- it legitimises your answers (we will check if your code really provides the answers you gave) and
- allows us to evaluate the approach you have taken.

Please keep the number of source code files to one; make a request to exempt you from this requirement the Brightspace forum in case this is not possible.

Don't forget to provide a [makefile](https://www.gnu.org/software/make/manual/html_node/Introduction.html) or script that allow us to compile your code.

## How you submit

The only way to submit your report and code is using git with this repository. 

An introduction to git is given in Brightspace (Content > Resources and Tools > Git introduction). Any problem you have with using Git, please refer to the FAQ in Brighspace. If that does not solve your issue, feel free to ask in the Brightspace forum (Collaboration > Discussions > General > Git and GitLab).

## Assessment

You will be given points for your correct answers; wrong answers receive a fraction of the total points or none. Each task has a pre-defined set of points, reported below. 

**Please note**:

- all answers must be given. If your answer sheet is not complete, you automatically fail. Report "none" or 0 if you want to want to skip that answer.
- your report is **individual**, which means:
  - you must use your code to find the answers you provide in the answer sheet, and
  - the code you submit must be of your authorship.
- we encourage you to cooperate with your colleagues at the **conceptual** level, so that you are safely within the requirements for an individual report mentioned above.

Referring to the [rubrics](https://brightspace.tudelft.nl/d2l/le/content/498874/viewContent/2663586/View), the grade is split according to:

- 20% Clarity
- 40% Approach
- 40% Content

## Types of answers

You can expect to provide the following types of answers:

- **numeric**, which are assessed by numeric comparison with our own solution, and fall in *Approach* item of the rubrics;
- **graphic**, generally composed of plots you produce, are assessed visually, and fall in *Clarity* and *Approach* items of the rubrics
- **open text**, related to answering questions on observations, interpretations and conclusions, generally from plot(s), which are assessed according to the *Content* and *Clarity* items of the rubrics.

An additional type of "answer" is the code you submit. It is assessed according to the *Approach* rubric item.

The table below illustrates how each type of "answer" relates to the rubrics items.

| Answer type   | Clarity | Approach | Content | Total | Points |
| ---           | ---     | ---      | ---     | ---   | ---    | 
| all           | 20%     | 40%      | 40%     |       | 80     | 
| numeric       |         | 1/2      |         | 20%   | 16     |
| graphic       |  1/2    | 1/4      |         | 20%   | 16     | 
| open text     |  1/2    |          | 1       | 50%   | 40     |
| code          |         | 1/4      |         | 10%   | 8      |

## Excellence

If you address all assignments tasks correctly, your final grade is 8. To get a higher grade, you have several opportunities to show excellence. There are two types of Excellence:

- Assignment Excellence, which is indicated in the assignment text by "**Opportunity for Excellence**", and
- [Coding Excellence](#coding-excellence)

Unlike Assignment Excellence, where each item is assigned specific points (see the *Final Remarks* section in the answer sheet), there is no specific formula for how much each Coding Excellence item is worth, because there are simply too many. Each one will be assessed individually.

We want to reward your efforts by being relatively liberal when grading Excellence. For example, you should get a 10 if your report is **completely correct** and you successfully address **a few** Assignment Excellence items and **a few** Coding Excellence items (see bellow). Likewise, you should get a very high mark if you address **most** Assignment and Coding Excellence items but some **a few** report answers incorrect. The wording above (*a few*, *most*) is deliberate because we will grade (Coding) Excellence on a case-by-case basis.

**Please note:** any Excellence points can _only_ be assessed if you list which Code and Assignment Excellence items you have addressed in the *Final remarks* section of your report.

## Coding excellence

In addition to opportunities for excellence specific to this assignment, there are the following (non-exhaustive list of) coding opportunities for excellence:

- improved execution efficiency,
- elements of automation,
- non-obvious, creative and/or innovative algorithmics, and
- unit testing. 
