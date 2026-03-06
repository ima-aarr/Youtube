import streamlit as st
import yt_dlp
import os

st.title("簡易YouTubeダウンローダー")
st.warning("※著作権フリーの動画、またはご自身が権利を持つ動画のバックアップ用途でのみご利用ください。")

url = st.text_input("YouTubeの動画URLを入力してください")

if st.button("動画を取得"):
    if url:
        with st.spinner("サーバー側で動画を処理中...（数十秒かかる場合があります）"):
       
            temp_filename = "downloaded_video.mp4"
            
       
            if os.path.exists(temp_filename):
                os.remove(temp_filename)

         
            ydl_opts = {
                'format': 'best',
                'outtmpl': temp_filename,
                'quiet': True,
                'noplaylist': True
            }

            try:
          
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
             
                if os.path.exists(temp_filename):
                    with open(temp_filename, "rb") as file:
                        st.success("処理が完了しました！下のボタンから保存してください。")
                        st.download_button(
                            label="動画をPC/スマホに保存する",
                            data=file,
                            file_name="video.mp4",
                            mime="video/mp4"
                        )
            except Exception as e:
                st.error(f"エラーが発生しました: {e}")
    else:
        st.warning("URLを入力してください。")
