import base64
import io
from PIL import Image
from filter.filter import *
import cv2


def get_image_download(img,filename,text):
    buffered = io.BytesIO()
    img.save(buffered,format='JPEG')
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =f'<a href="data:file/txt;base64,{img_str}" download="{filename}">{text}</a>'
    return href


st.title("Artistic Image filters")

upload_file = st.file_uploader('upload an imaage file',type=['png','jpg'])

if upload_file is not None:
    raw_bytes = np.asarray(bytearray(upload_file.read()),dtype=np.uint8)
    img = cv2.imdecode(raw_bytes,cv2.IMREAD_COLOR)
    input_col,output_col = st.columns(2)
    with input_col:
        st.header('Orginal')
        st.image(img,channels='BGR',use_column_width=True)

    st.header('Filter Example:')
    option= st.selectbox('Select a filter:',(
        'None',
        'Black and White',
        'Sepia / Vintage',
        'Vignette Effect',
        'Pencil Sketch'
    ))
    col1,col2,col3,col4=st.columns(4)
    imgs = cv2.imread('butterfly.jpg')
    with col1:
        st.caption('Black and white')
        st.image( bw_filter(imgs))

    with col2:
        st.caption('Sepia / Vintage')
        st.image( sepia(imgs))

    with col3:
        st.caption('Vignette Effect')
        st.image( vignette(imgs,level=4))

    with col4:
        st.caption( 'Pencil Sketch')
        st.image(pencile(imgs,ksize=5))

    output_flag = 1
    color ='BGR'
    output=None


    if option == 'None':
        output_flag =0
    elif option == 'Black and White':
        output = bw_filter(img)
        color='GRAY'
    elif option == 'Sepia / Vintage':
        output = sepia(img)
    elif option == 'Vignette Effect':
        level = st.slider('level',0,5,2)
        output = vignette(img,level)
    elif option == 'Pencil Sketch':
        ksize = st.slider('Blur Kernal size',1,11,5,step=2)
        output = pencile(img,ksize)
        color='GRAY'
    with output_col:
        if output_flag ==1:
            st.header('Output')
            st.image(output,channels=color)
            if color == 'BGR':
                result = Image.fromarray(output[:,:,::-1])
            else:
                result = Image.fromarray(output)
            st.markdown(get_image_download(result,'output.png','Download '+'Output'),unsafe_allow_html=True)



#

