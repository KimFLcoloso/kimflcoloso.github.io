# generate_md.py
md_content = """# 제목
이곳에 마크다운 내용을 작성합니다.
"""

# `.md` 파일을 posts 폴더에 저장합니다.
with open('posts/generated_post.md', 'w') as file:
    file.write(md_content)
