from makejinja.cli import makejinja_cli

def main():
    # Create a simple template string
    template = "Hello, {{ name }}!"
    
    # Create a simple context dictionary
    context = {"name": "World"}
    
    # Call makejinja_cli with the template and context
    result = makejinja_cli(template_str=template, context_dict=context)
    
    print(result)

if __name__ == "__main__":
    main()