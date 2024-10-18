---
title: "Sample Markdown Document"
author: "Your Name"
date: "2024-10-18"
toc: true
---

# Table of Contents
<!-- This will generate a table of contents automatically if using tools like Pandoc -->
[TOC]

# Introduction
This document is a demonstration of various features in Markdown, including a table of contents, a table with data, and a Mermaid flow diagram. Markdown is an easy-to-use language for formatting text.

# Section 1: Overview
Markdown allows you to structure your document with headings. You can use different levels of headings to create sections and subsections.

## Subsection 1.1: Key Points
- **Easy to use**: Markdown is simple and intuitive.
- **Flexible**: Supports tables, diagrams, and more.
- **Portable**: Can be converted to other formats like PDF.

# Section 2: Table of Data
Here is an example of a table in Markdown. Tables are useful for organizing data in a structured format.

| Name         | Age | Occupation   |
|--------------|-----|--------------|
| John Doe     | 30  | Engineer     |
| Jane Smith   | 25  | Designer     |
| Alice Brown  | 35  | Data Analyst |

# Section 3: Flow Diagram
You can include a **Mermaid** flow diagram in Markdown to visually represent processes or flows. Here's a simple example:

```mermaid
graph TD;
    A[Start] --> B{Decision};
    B -->|Yes| C[Process 1];
    B -->|No| D[Process 2];
    C --> E[End];
    D --> E;
