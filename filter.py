import json
import re

bad_attr = [
    "onclick",
    "ondblclick",
    "onchange",
    "onblur",
    "onfocus",
    "onkeydown",
    "onkeypress",
    "onkeyup",
    "onmousedown",
    "onmousemove",
    "onmouseover",
    "onmouseout",
    "onmouseup",
    "onselect",
    "onsubmit",
    "onreset",
    "onload",
    "onabort",
    "onerror",
    "src",
]

# Match style tags
style_tags = r"<style[^>]*>[^<]*<\/style>"

# Match script tags
script_tags = r"<script[^>]*>[^<]*<\/script>"

# Match img tags
img_tags = r"<img[^>]*>[^<]*<\/img>"

# Match iframe tags
iframe_tags = r"<iframe[^>]*>[^<]*<\/iframe>"

# Match attributes
all_attr = r"("+'|'.join(bad_attr)+r")\s*=\s*(\"([^\"]*)\"|'([^']*)'|([^ >]*))"

def filter_script_tags(html):
    return re.sub(script_tags, '', html)


def filter_style_tags(html):
    return re.sub(style_tags, '', html)
    
    
def filter_img_tags(html):
    return re.sub(img_tags, '', html)
    
    
def filter_iframe_tags(html):
    return re.sub(iframe_tags, '', html)


def filter_bad_attr(html):
    return re.sub(all_attr, '', html)


def lambda_handler(event, context):
    initial = event['raw_html']
    no_script = filter_script_tags(initial)
    no_style = filter_style_tags(no_script)
    no_img = filter_img_tags(no_style)
    no_iframe = filter_iframe_tags(no_img)
    no_bad_attr = filter_bad_attr(no_iframe)
    return {
        'statusCode': 200,
        'body': json.dumps('Success!'),
        'filtered_html': no_bad_attr
    }

