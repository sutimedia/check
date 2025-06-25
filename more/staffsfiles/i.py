# Generate HTML <img> tags for images SB (1) to SB (108) with 100% width
for i in range(1, 109):
    print(f'<img src="../../assets/img/gallary/SB ({i}).jpg" class="img-fluid mx-2 mb-2" style="max-width: 320px; max-height: 305px; margin-bottom: 2px">')
