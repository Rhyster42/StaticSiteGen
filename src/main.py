import os, shutil, sys
from pathlib import Path

from blocks import markdown_to_html_node
from extractors import extract_title

    
def import_directory(source, target_directory):

    if os.path.exists(target_directory):
        
        shutil.rmtree(target_directory)

    os.mkdir(target_directory)

    for filename in os.listdir(source):
        source_path = os.path.join(source, filename)
        target_path = os.path.join(target_directory, filename)

        if os.path.isfile(source_path):
            print(f"Copying file: {source_path} to {target_path}")
            shutil.copy(source_path, target_path)
        else:
            print(f"Creating directory: {target_path}")
            import_directory(source_path, target_path)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path, basepath):

    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path, 'r') as f:
        from_doc = f.read()

    with open(template_path, 'r') as f:
        template = f.read()


    html_md_string = markdown_to_html_node(from_doc).to_html()


    header = extract_title(from_doc)
    final_md = template.replace('{{ Title }}', header)\
        .replace('{{ Content }}', html_md_string)\
        .replace('href="/', f'href="{basepath}')\
        .replace('src="/', f'src="{basepath}')

    print(f"os.path.dirname({dest_path}) evaluates to: {os.path.dirname(dest_path)}")
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(final_md)

    pass

def main():

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'
    print(f'____________________{basepath}__________________')

    target_directory = '/home/rhysespich/workspace/StaticSiteGen/docs'
    source_directory = '/home/rhysespich/workspace/StaticSiteGen/static'
    import_directory(source_directory,target_directory)

    content_dir = '/home/rhysespich/workspace/StaticSiteGen/content'
    template_path = '/home/rhysespich/workspace/StaticSiteGen/template.html'
    
    

    generate_pages_recursive(content_dir, template_path, target_directory)
            
    

if __name__ == "__main__":
    main()