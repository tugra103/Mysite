from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

URL = "https://eu3-browse.startpage.com/av/proxy?ep=5047493649324974666a4572497a4d32637a64304d486b704e7941314e337073515870674132467a42534d794d33456d62796f6d43596b625463714b587074526e7068417955784d33463241447336637a516d4b6a526b635749744b48707352437367597a64384e44456e59696f375953737a65434a304a6d5967494770734e323478636e5a34495778334a573037596d786a664831346357456e646d31734a69736865416b56494759494c68596c5467733164516b6d5a6d6342595777624a6977696548636c647a496e644431754f5759324979556a4a546438644778755a4764716379456b49545639646d64734a69733649436b6b666a41674d6a59385a586b6c654149674c7963675969387363324a6a&ek=58313953525552425131524652463966&ekdata=3ef8b7652ade35a557084bd09a884c56&sc=7JqRfQOsPNoD20"

@app.route("/iframe", methods=["GET"])
def get_iframe():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        iframe = soup.find("iframe")

        if iframe and iframe.has_attr("src"):
            iframe_url = iframe["src"]
            return jsonify({"iframe_url": iframe_url})
        else:
            return jsonify({"error": "iframe bulunamadı veya src yok"}), 404

    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
