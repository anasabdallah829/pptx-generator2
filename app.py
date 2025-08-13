def render_slide_preview(slide_analysis):
    """عرض معاينة تفاعلية للشريحة مع placeholders"""
    if not slide_analysis:
        return
    
    dimensions = slide_analysis['slide_dimensions']
    
    # زيادة مساحة العرض للحصول على وضوح أفضل
    max_width = 1024
    aspect_ratio = dimensions['width'] / dimensions['height']
    
    if aspect_ratio > 1:  # عرض أكبر من الارتفاع
        display_width = max_width
        display_height = max_width / aspect_ratio
    else:  # ارتفاع أكبر من العرض
        display_height = max_width
        display_width = max_width * aspect_ratio
    
    st.markdown(f"""
    <div style="
        width: {display_width}px; 
        height: {display_height}px; 
        border: 2px solid #ddd; 
        position: relative; 
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        margin: 20px auto;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        overflow: hidden;
    ">
        <div style="
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(0,0,0,0.7);
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 12px;
            z-index:2;
        ">
            أبعاد الشريحة: {dimensions['width_inches']:.1f}" × {dimensions['height_inches']:.1f}"""
        </div>
    """, unsafe_allow_html=True)
    
    # عرض placeholders
    placeholder_html = ""
    
    # عرض صور placeholders
    for i, placeholder in enumerate(slide_analysis['image_placeholders']):
        left = (placeholder['left_percent'] / 100) * display_width
        top = (placeholder['top_percent'] / 100) * display_height
        width = (placeholder['width_percent'] / 100) * display_width
        height = (placeholder['height_percent'] / 100) * display_height
        
        placeholder_html += f"""
        <div style="
            position: absolute;
            left: {left}px;
            top: {top}px;
            width: {width}px;
            height: {height}px;
            border: 2px dashed #ff6b6b;
            background: rgba(255, 107, 107, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 14px;
            color: #ff6b6b;
            font-weight: bold;
            border-radius: 5px;
            z-index:3;
        ">
            🖼️ صورة {i+1}
        </div>
        """
    
    # عرض text placeholders
    for i, placeholder in enumerate(slide_analysis['text_placeholders']):
        left = (placeholder['left_percent'] / 100) * display_width
        top = (placeholder['top_percent'] / 100) * display_height
        width = (placeholder['width_percent'] / 100) * display_width
        height = (placeholder['height_percent'] / 100) * display_height
        
        placeholder_html += f"""
        <div style="
            position: absolute;
            left: {left}px;
            top: {top}px;
            width: {width}px;
            height: {height}px;
            border: 2px dashed #4ecdc4;
            background: rgba(78, 205, 196, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            color: #4ecdc4;
            font-weight: bold;
            border-radius: 5px;
            text-align: center;
            padding: 2px;
            z-index:3;
        ">
            📝 نص {i+1}
        </div>
        """
    
    # عرض title placeholders
    for i, placeholder in enumerate(slide_analysis['title_placeholders']):
        left = (placeholder['left_percent'] / 100) * display_width
        top = (placeholder['top_percent'] / 100) * display_height
        width = (placeholder['width_percent'] / 100) * display_width
        height = (placeholder['height_percent'] / 100) * display_height
        
        placeholder_html += f"""
        <div style="
            position: absolute;
            left: {left}px;
            top: {top}px;
            width: {width}px;
            height: {height}px;
            border: 2px dashed #45b7d1;
            background: rgba(69, 183, 209, 0.15);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            color: #45b7d1;
            font-weight: bold;
            border-radius: 5px;
            z-index:3;
        ">
            📋 عنوان
        </div>
        """
    
    st.markdown(placeholder_html + "</div>", unsafe_allow_html=True)