# Experiments with BERT and Transformers

## Infer masked token with BERT

### Description

BERT's authors trained it in two tasks and one of them is **Masked Language Model** (MLM). The task consists of mask some input tokens randomly, and then try to predict those random tokens. Hence, we do not need to pretrain BERT and we can directly test it,

In this repository, I have implemented **a basic script to infer the masked token** in a sentence.

Read the BERT paper: https://arxiv.org/pdf/1810.04805.pdf

### Code

With this repository, there are some commands in Bash to run the Python code in a Docker container. Anyway, you can find all the Python scripts at [./code](./code)

You can see the code execution step by step in the notebooks (see folder [./notebooks](./notebooks)). Additionally, the notebooks are available at Kaggle:
- https://www.kaggle.com/dimasmunoz/infer-masked-token-with-bert

### Commands

> Note: These commands have been tested in MacOS and Git Bash (Windows).

You can start/stop the docker container with these two commands:
```sh
sh manager.sh docker:run
sh manager.sh docker:down
```

Once the docker container is running, execute the BERT script as follows:
```sh
sh manager.sh bert
```

Then, it will display a prompt where you can write your sentences with a masked token. For example:
```
$ sh manager.sh bert
Downloading: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████| 996k/996k [00:02<00:00, 485kB/s]
Downloading: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 625/625 [00:00<00:00, 176kB/s]
Downloading: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 714M/714M [01:07<00:00, 10.7MB/s]

Input text: This is a [MASK] model
----------------------------------------
mathematical 0.04100513085722923
model 0.03972144424915314
single 0.01666860282421112
similar 0.014901496469974518
common 0.01419056300073862
========================================

...
```

## Question-answering with BERT

### Description

In Question-Answering tasks, the model receives a text and a question regarding to the text, and it should mark the beginning and end of the answer in the text.

In this case, it is necessary to fine-tune BERT. We will use XQuAD (Cross-lingual Question Answering Dataset) to fine-tune it, which consists of a subset of 240 paragraphs and 1190 question-answer pairs from the development set of SQuAD v1.1 together with their professional translations into 10 languages. Source: https://github.com/deepmind/xquad

### Code

You can see the code execution step by step in the notebooks (see folder [./notebooks](./notebooks)).


Have fun! ᕙ (° ~ ° ~)
