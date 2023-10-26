#!/bin/bash
pandoc -f markdown -t docx --reference-doc=template.docx -o ColinWilsonResume.docx resume.md
