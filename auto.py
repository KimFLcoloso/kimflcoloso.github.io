# generate_md.py
md_content = """---
published: true
layout: post
title: "자동 테스트"
---

## h2
이곳에 마크다운 내용을 작성합니다.
"""

# `.md` 파일을 posts 폴더에 저장합니다.
with open('_posts/2024-03-05-post.md', 'w') as file:
    file.write(md_content)
