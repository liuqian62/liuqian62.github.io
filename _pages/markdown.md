---
permalink: /markdown/
title: "Markdown写作教程"
author_profile: true
redirect_from: 
  - /md/
  - /markdown.html
---
## 目录
- [关键文件目录](#关键文件目录)
- [Markdown指南](#Markdown指南)
- [HTML标签](#HTML标签)

## 关键文件目录

* Basic config options: _config.yml
* Top navigation bar config: _data/navigation.yml
* Single pages: _pages/
* Collections of pages are .md or .html files in:
  * _publications/
  * _portfolio/
  * _posts/
  * _teaching/
  * _talks/
* Footer: _includes/footer.html
* Static files (like PDFs): /files/
* Profile image (can set in _config.yml): images/profile.png

## 提示

* Name a file ".md" to have it render in markdown, name it ".html" to render in HTML.
* Go to the [commit list](https://github.com/academicpages/academicpages.github.io/commits/master) (on your repo) to find the last version Github built with Jekyll. 
  * Green check: successful build
  * Orange circle: building
  * Red X: error
  * No icon: not built

## Resources
 * [Liquid syntax guide](https://shopify.github.io/liquid/tags/control-flow/)


<div align="right">
    <b><a href="#目录">↥ Back To Top</a></b>
</div>


## Markdown指南

### Header three

#### Header four

##### Header five

###### Header six

## 块引用

Single line blockquote:

> Quotes are cool.

## Tables

### Table 1

| Entry            | Item   |                                                              |
| --------         | ------ | ------------------------------------------------------------ |
| [John Doe](#)    | 2016   | Description of the item in the list                          |
| [Jane Doe](#)    | 2019   | Description of the item in the list                          |
| [Doe Doe](#)     | 2022   | Description of the item in the list                          |

### Table 2

| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|-----------------------------|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|=============================|
| Foot1   | Foot2   | Foot3   |

## 定义列表

定义列表标题
:   Definition list division.

Startup
:   A startup company or startup is a company or temporary organization designed to search for a repeatable and scalable business model.

#dowork
:   Coined by Rob Dyrdek and his personal body guard Christopher "Big Black" Boykins, "Do Work" works as a self motivator, to motivating your friends.

Do It Live
:   I'll let Bill O'Reilly [explain](https://www.youtube.com/watch?v=O_HyZ5aW76c "We'll Do It Live") this one.

## 无序列表 (嵌套)

  * List item one 
      * List item one 
          * List item one
          * List item two
          * List item three
          * List item four
      * List item two
      * List item three
      * List item four
  * List item two
  * List item three
  * List item four

## 有序列表 (嵌套)

  1. List item one 
      1. List item one 
          1. List item one
          2. List item two
          3. List item three
          4. List item four
      2. List item two
      3. List item three
      4. List item four
  2. List item two
  3. List item three
  4. List item four

## 按钮

Make any link standout more when applying the `.btn` class.

## 通知

**Watch out!** You can also add notices by appending `{: .notice}` to a paragraph.
{: .notice}


<div align="right">
    <b><a href="#目录">↥ Back To Top</a></b>
</div>


## HTML标签

### 地址 Tag

<address>
  1 Infinite Loop<br /> Cupertino, CA 95014<br /> United States
</address>

### Anchor Tag (aka. 链接)

This is an example of a [link](http://github.com "Github").

### 缩写

The abbreviation CSS stands for "Cascading Style Sheets".

*[CSS]: Cascading Style Sheets

### 引用

"Code is poetry." ---<cite>Automattic</cite>

### 代码

You will learn later on in these tests that `word-wrap: break-word;` will be your best friend.

### 删除

This tag will let you <strike>strikeout text</strike>.

### 强调

The emphasize tag should _italicize_ text.

### 插入

This tag should denote <ins>inserted</ins> text.

### 键盘标签

This scarcely known tag emulates <kbd>keyboard text</kbd>, which is usually styled like the `<code>` tag.

### 预格式化标签

This tag styles large blocks of code.

<pre>
.post-title {
  margin: 0 0 5px;
  font-weight: bold;
  font-size: 38px;
  line-height: 1.2;
  and here's a line of some really, really, really, really long text, just to see how the PRE tag handles it and to find out how it overflows;
}
</pre>

### 引号

<q>Developers, developers, developers&#8230;</q> &#8211;Steve Ballmer

### 加粗

This tag shows **bold text**.

### 下标

Getting our science styling on with H<sub>2</sub>O, which should push the "2" down.

### 上标

Still sticking with science and Isaac Newton's E = MC<sup>2</sup>, which should lift the 2 up.

### 变量

This allows you to denote <var>variables</var>.


<div align="right">
    <b><a href="#目录">↥ Back To Top</a></b>
</div>

