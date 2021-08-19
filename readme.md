# Question Extractor

Author - Delta0001#8468

Code hosted on GitHub at [Question-Extractor](https://github.com/SuperSat001/Question-Extractor)


## Usage Instructions

- Open `code.py` and on Line 36, write the name of your file. 
If file is a `.png` then `pics()` function can be used, if `.pdf` then `pdfs()`
On Line 38, the second arguement of `cli()` function is the first question number of the file. Edit accordingly.

- Run `code.py` (please prefer using an IDE over terminal here as windows terminal was sometimes not taking `Ctrl+C` while code was running)

- Tkinter window will open. Main image is under `Current Question` on which operations below are going to be performed. 

## Commands


### While Not Merging

1. **Skip**. 
	- To skip `Current Question`

2. **Save**
	- To save `Current Question`

3. **Start Merge**
	- When you see the `Next Question` should be merged with `Current Question` start merge.


### While Not Merging

Update - Now that you can manually set `Q No.` you can use 3rd command for both 3 and 4 and then change numbers manually, in case it's unclear when to use 3 and 4, use 3 and adjust.

1. **Skip While Merging**. 
	- To skip `Current Question` but continue merging, `Current Merge` remains same.

2. **Save End Merge**
	- To save `Current Question` and end `Current Merge`. Closely related to 5.

3. **Merge Same**
	- When you want to merge `Current Question` to `Current Merge` but not change `Q No.`. Like suppose there is a paragraph from q1-4 and before q1 there is paragraph statement. So when paragraph statement is `Current Question` then you'll `Start Merge` and when `q1` is `Current Question` then you will use **this command** to merge statement and q1.

4. **Merge Next**
	- Continuing last example, after you have used `Start Merge` and `Merge Same`, your `Current Merge` is comprised of `statement-q1`. Now when q2 is `Current Question`, use **this command** to merge q2 with `Current Merge` and increase `Q No.`

5. **Skip End Merging**. 
	- To skip `Current Question` and save `Current Merge`. In the pervious example, after you have merged `statement-q1-q2-q3-q4` and next image has to be skipped, use this. 

### Q Inc and Q Dec
In case you need to change `Q No.` (note that it's the **next** question number to be saved), you can use `Q Inc` to increase and `Q Dec` to decrease. Make sure that when you are saving multiple merged questions, `Q No.` is the last question number of the merged qns.

## Note

- I know that `While Not Merging` command appears a bit complicated but after 2-3 uses you will be comfortable

- `Last <x>` just keeps track of last button pressed.

- `pdf2image` is a bit slow, suggest me new libraries.

- Make sure the program successfully terminates in-case you close the `Tkinter` window in between. It's kinda wack.

