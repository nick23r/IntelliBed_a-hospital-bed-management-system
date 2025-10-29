from PIL import Image

# Add CUBIC as an alias for BICUBIC for backwards compatibility
if not hasattr(Image, 'CUBIC'):
    setattr(Image, 'CUBIC', Image.Resampling.BICUBIC)