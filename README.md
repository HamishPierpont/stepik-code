# Stepik code

This repository contains a generic template, written in Python,
for the backend of Stepik problems. It also contains a .step file
that can be uploaded directly to Stepik and edited, which streamlines
the process of adding a new coding problem to Stepik.

## Installation

Clone this repository locally. If you decide to modify `stepik_backend.py`, make a copy of the
file and put your work in there; this ensures a clean copy of the template
is maintained.

## Usage

Please take a look at this [Google doc](https://docs.google.com/document/d/14o13L9Mvg-zMp1JQFzt08TIAi8gjIu3vpgOWPpe68XE/edit#heading=h.8k3ipcbozllc)
for a detailed usage guide.

Download template and sample .step file from GitHub.
Users familiar with git should clone their repository to their local machine using git clone or the
GitHub CLI. Downloading the files as a .zip archive is also okay.

Inside this git repository is the python backend code and a sample .step file.
The .step file has the backend code as one of its fields, so you shouldn’t need to directly edit the
backend file. Uploading the .step file to stepik and editing there should be sufficient.

### How is Stepik structured?
Stepik courses are broken up into modules. Each module has one or more lessons, with each lesson
containing one or more steps. These “steps” could be one of twenty-one different types, including
math problems, text lessons, or videos; however, each step in Stepik as of 1/14/2020 is a “coding
challenge,” where students can type in code to solve a problem and then submit it for automatic
grading.

For COP3530, each module addresses a broad topic from the class, like heaps or trees. The lessons
map to a sub-topic: within the Trees module, there are lessons for n-ary trees, binary trees, an
binary search trees. Each lesson contains coding challenge steps meant to test students’
understanding of the material.

### Adding a new module with lessons to Stepik
1. Go to Stepik.
2. Click the course you want to edit.
3. Click “Edit course syllabus”.
4. Scroll all the way down and click “+ New module”.
5. Once the module is created, give it a name.
6. Also type a new name for the lessons you would like to make and press “+ Create lesson”.
7. Press save, then press back.

You have now created a module.

By default, a newly-created lesson will have one step in it. This step will be a Text step, and it
won’t have any useful info. Once you have created coding challenge steps, feel free to delete this
automatically-created Text step.

### Adding a new step (coding problem) to a lesson
1. Within Stepik, scroll down to the lesson you want to add a problem to and click the lesson’s name.
2. Now press “Edit”.
3. Create a new step with type “code challenge”.
4. Now at the bottom inside the new step press “Step Actions”, then press “upload step”.
5. Upload the template step “sample.step” provided on the github repository.
6. Now edit the step to match the problem you wish to add.


### How does Stepik test student code?
When a student types code into the Stepik frontend and hits “Submit”, their code is pasted into the
C++ source file outlined in "Languages & Templates. This file contains a main method. This source
file is compiled on Stepik’s remote server. Immediately after this, the stepik backend written in
Python will use the `generate` function to produce a series of test cases. These test cases will be
combined with any test cases in the frontend (with the frontend test case(s) first and the backend 
test case(s) second) and then fed, one-by-one, as (standard) input to the executable. The executable
will then print text to stdout. The python backend will pick this text up and compare it to the
expected output for the test case. If they match, the student gets credit for this test case. Note
that the backend strips leading and trailing whitespace from the expected and actual outputs, so
there’s no need for a perfect match. If the student output does not match the expected output, they
fail the test case; the input will be shown to them to aid in debugging (the complexity of the
stepik_backend.py file comes from orchestrating this display).

### Cool. How do I set up this backend?
1. Go to the desired step within the stepik course.
2. Go to “Edit” within the lesson.
3. Add desired text, images, code samples, etc. to problem description.
4. At the bottom there will be 3 tabs: “Test Cases”, “Languages and Templates”, and “Advanced”.
5. Create desired test case inputs and outputs on your own, outside of stepik. You can test them out
   in stepik if you would like as well.
6. Click “Test Cases”. Place the first test case input and output here. Do not add others here, only
   have the first [<sup id="footnote-id">1</sup>](#fn1). 
7. Click “Languages and Templates”.
   * “::c++” means that the code solution can be in c++, if we were to add “::python3” below it, solutions in python would also be accepted. But just “::c++” will do; just use that one assuming the class will be in cpp.
   * Hidden templates can be useful to define auxiliary functions and data input/output, to prevent the usage of certain functions/libraries, and to perform additional checks on student's code.
   * Under “::header” is where you place anything to be hidden from students in the header, i.e. including libraries and supplementary class/function definitions.
   * Under “::footer” is where you put c++ code hidden from students in the footer, possibly to put a main function, to take in the input and output the desired outputs. 
   * The code that students write will go under “::code”. Here is where you place template code students will start off with, i.e. function/class wrappers. You can look at other steps for examples.
8. Click “Advanced”. 
   * Within the code find “tests = []” and “correct_answers = []”. Here is where you will put the REST OF the corresponding test case inputs and outputs as strings, starting with the second one all the way to the last one. If an input or output is more than one line, represent the new line as “\n”; be careful for unwanted spaces in the input/output.
   * An example: 
   ```{python3}
   tests = [
   "5\n1->2->4", 
   "5\n5->3->2"
   ]
   
   correct_answers = [ "-1", "0" ]
   ```

9. Press “Save changes”  and then “back” to go back to the stepik lesson.
Test it out to make sure it works!

## Contribution

Please feel free to update the template with improvements as necessary.
Avoid committing specific implementations of the backend to this repository
(e.g., a copy of the template filled out with tests and correct answers for
problem **8.1.2** in the course Stepik page); this repository is meant to keep
track of changes to the template, not changes to the backend for individual
problems.

### Footnotes
1. <span id="fn1"></span> [.](#footnote-id). Stepik breaks if the first test case isn’t in the frontend. We tried to get Stepik to fix this, but they don’t seem to care about instructor experience.