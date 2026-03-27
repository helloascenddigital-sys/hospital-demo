import re
import sys

def patch_departments(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    images = [
        ('gen_medicine.png', 'General Medicine'),
        ('orthopaedics.png', 'Orthopaedics'),
        ('neurology.png', 'Neurology'),
        ('emergency.png', 'Emergency & Critical Care'),
        ('pediatrics.png', 'Pediatrics'),
        ('gynecology.png', 'Gynecology'),
        ('diagnostics.png', 'Diagnostics & Labs'),
        ('pulmonology.png', 'Pulmonology'),
    ]

    for img, title in images:
        # Find the card block for this title
        pattern = re.compile(r'(<div class="card[^>]*>).*?(?<=\s\s)(<div style="display: flex; justify-content: center;">\s*<div class="icon-wrap.*?</p>\s*</div>)', re.DOTALL | re.IGNORECASE)
        
        # We need a more specific search. Let's find the card that contains the title.
        # title is like '<h3>General Medicine</h3>'
        
        # A simpler approach: find <h3>Title</h3> and work backwards to <div class="card">
        # Or just regex over the whole file
        pass

    # Actually simpler:
    new_content = content
    
    def replacer(match, img_name):
        class_attr = match.group(1)
        inner = match.group(2)
        
        # If already patched, skip
        if '<img' in inner: return match.group(0)
        
        # Add style="padding: 0; overflow: hidden;" to the card block
        if 'style="' in class_attr:
            class_attr = class_attr.replace('style="', 'style="padding: 0; overflow: hidden; ')
        else:
            class_attr = class_attr.replace('class="', 'style="padding: 0; overflow: hidden;" class="')
            
        new_inner = inner.replace('<div style="display: flex; justify-content: center;">', f'<img src="images/{img_name}" style="width: 100%; height: 200px; object-fit: cover; display: block;" alt=""><div style="padding: 25px;"><div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">')
        # find the end of the card and add </div> before it
        # Actually we just append </div> at the end of the match inner
        new_inner = new_inner.replace('</p>', '</p></div>')
        return class_attr + new_inner + '\n                </div>'
        
    replacements = [
        ('General Medicine', 'gen_medicine.png'),
        ('Orthopaedics', 'orthopaedics.png'),
        ('Neurology', 'neurology.png'),
        ('Emergency & Critical Care', 'emergency.png'),
        ('Pediatrics', 'pediatrics.png'),
        ('Gynecology', 'gynecology.png'),
        ('Diagnostics & Labs', 'diagnostics.png'),
        ('Pulmonology', 'pulmonology.png')
    ]
    
    for title, img_name in replacements:
        # Match from <div class="card ..."> to </div> containing the specific h3
        pattern = re.compile(r'(<div class="card[^>]*>)(.*?' + re.escape(f'<h3>{title}</h3>') + r'.*?</p>\s*)</div>', re.DOTALL)
        
        def rep_func(m):
            card_open = m.group(1)
            content_inner = m.group(2)
            
            if 'padding: 0; overflow: hidden;' not in card_open:
                if 'style="' in card_open:
                    card_open = card_open.replace('style="', 'style="padding: 0; overflow: hidden; ')
                else:
                    card_open = card_open.replace('>', ' style="padding: 0; overflow: hidden;">')
                    
            if '<img src=' not in content_inner:
                content_inner = content_inner.replace('<div style="display: flex; justify-content: center;">', f'<img src="images/{img_name}" alt="{title}" style="width: 100%; height: 200px; object-fit: cover; display: block;">\n                    <div style="padding: 25px;">\n                        <div style="display: flex; justify-content: center; margin-top: -55px; position: relative;">')
                content_inner = content_inner.replace('fas fa-', 'fas fa-', 1) # dummy
                # Wrap icon wrap with background white
                content_inner = content_inner.replace('class="icon-wrap', 'style="background: white; border: 4px solid var(--color-bg-light); box-shadow: var(--shadow-md);" class="icon-wrap')
                content_inner = content_inner + "</div>\n                "
                
            return card_open + content_inner + "</div>"

        new_content = pattern.sub(rep_func, new_content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Patched {filepath}")

patch_departments('departments.html')
