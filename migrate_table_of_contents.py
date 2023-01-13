import os
import sys

if __name__ == "__main__":
    toc_table = """
# Table of Contents
| Project | Description |
| --- | --- |
"""
    for root, folder, file in os.walk("./projects/"):
        if root == "./projects/":
            continue
        if file.count("README.md"):
            with open(os.path.join(root, "README.md")) as f:
                title = ""
                description = ""
                readme = f.read()
                lines = readme.splitlines()
                index_of_title = 0
                for i in lines:
                    if i.startswith("#"):
                        title = i[2:]
                        break
                    index_of_title += 1
                if not title:
                    sys.exit("No title found")
                print(f"title: {title}")
                description = lines[index_of_title+1]
                print(f"description: {description}")
            toc_table += f"""| [{title}]({root}/README.md) | {description} |"""

    main_readme = open("README.md").read()
    main_readme_lines = main_readme.splitlines()
    try:
        start_index_of_toc = main_readme_lines.index("# Table of Contents")
    except ValueError:
        sys.exit("No table of contents found in README.md")
    try:
        end_index_of_toc = main_readme_lines.index(
            "<!--Table of contents end, do not remove this comment -->")
    except ValueError:
        sys.exit("No end of table of contents found in README.md")

    contents_before_toc_table = "\n".join(
        main_readme_lines[:start_index_of_toc])
    contents_after_toc_table = "\n".join(main_readme_lines[end_index_of_toc:])

    new_readme = f"""{toc_table}
    """

    with open("README.md", "w") as f:
        f.write(new_readme)
