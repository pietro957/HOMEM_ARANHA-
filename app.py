import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Homem-Aranha & Kuromi", page_icon="🖤", layout="centered")

st.title("Homem-Aranha & Kuromi 🖤")
st.write("Clica no Homem-Aranha no topo do prédio!")

# HTML/CSS/JS da animação interativa
html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
    body {
        margin: 0;
        background-color: #141828;
        font-family: Arial, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 500px;
        overflow: hidden;
    }
    #cenario {
        position: relative;
        width: 100%;
        max-width: 600px;
        height: 480px;
        background-color: #141828;
        border-radius: 10px;
        overflow: hidden;
        border: 2px solid #333;
    }
    .chao {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 30px;
        background-color: #1e1e1e;
    }
    .predio {
        position: absolute;
        bottom: 30px;
        left: 80px;
        width: 180px;
        height: 300px;
        background-color: #282d3c;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        padding: 20px 15px;
        box-sizing: border-box;
    }
    .janela {
        background-color: #f0dc64;
        height: 25px;
        border-radius: 3px;
    }
    /* Homem-Aranha */
    #aranha {
        position: absolute;
        top: 100px; /* Topo do prédio */
        left: 145px;
        width: 40px;
        height: 50px;
        cursor: pointer;
        transition: top 1.2s cubic-bezier(0.55, 0.055, 0.675, 0.19);
        z-index: 5;
    }
    .cabeca-aranha {
        width: 30px;
        height: 30px;
        background-color: #c81e1e;
        border-radius: 50%;
        margin: 0 auto;
        position: relative;
    }
    .olho {
        position: absolute;
        width: 8px;
        height: 12px;
        background: white;
        border-radius: 50% 50% 0 50%;
        top: 8px;
    }
    .olho.esq { left: 5px; transform: rotate(-15deg); }
    .olho.dir { right: 5px; transform: rotate(15deg) scaleX(-1); }
    .olho.morto {
        background: none;
        color: black;
        font-weight: bold;
        font-size: 14px;
        top: 5px;
        left: 7px;
        border-radius: 0;
    }
    .corpo-aranha {
        width: 26px;
        height: 25px;
        background-color: #c81e1e;
        border-radius: 8px;
        margin: -5px auto 0;
    }

    /* Kuromi */
    #kuromi {
        position: absolute;
        bottom: 30px;
        right: 80px;
        width: 45px;
        height: 50px;
        transition: right 1.2s linear;
        z-index: 4;
    }
    .cabeca-k {
        width: 40px;
        height: 35px;
        background-color: #2d3748;
        border-radius: 50%;
        position: relative;
        margin: 0 auto;
    }
    .orelha-k {
        position: absolute;
        width: 0; height: 0;
        border-left: 9px solid transparent;
        border-right: 9px solid transparent;
        border-bottom: 16px solid #2d3748;
        top: -10px;
    }
    .orelha-k.esq { left: 1px; transform: rotate(-20deg); }
    .orelha-k.dir { right: 1px; transform: rotate(20deg); }
    .caveira {
        position: absolute;
        width: 10px;
        height: 8px;
        background: #f687b3;
        border-radius: 50%;
        top: 10px;
        left: 15px;
    }
    .olho-k {
        position: absolute;
        width: 6px;
        height: 6px;
        background: #fff;
        border-radius: 50%;
        top: 16px;
    }
    .olho-k.esq { left: 10px; }
    .olho-k.dir { right: 10px; }
    .corpo-k {
        width: 30px;
        height: 20px;
        background-color: #fff;
        border-radius: 10px;
        margin: -5px auto 0;
    }

    /* Balão de Fala e Coração */
    #balao {
        display: none;
        position: absolute;
        bottom: 110px;
        left: 110px;
        background: white;
        color: #333;
        padding: 10px 15px;
        border-radius: 15px;
        font-weight: bold;
        font-size: 16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        z-index: 10;
    }
    #balao::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 30px;
        border-width: 10px 10px 0;
        border-style: solid;
        border-color: white transparent;
        display: block;
        width: 0;
    }
    #coracao {
        display: none;
        position: absolute;
        bottom: 75px;
        left: 175px;
        font-size: 24px;
        animation: pulso 0.6s infinite alternate;
        z-index: 6;
    }
    @keyframes pulso {
        from { transform: scale(1); }
        to { transform: scale(1.3); }
    }
</style>
</head>
<body>

<div id="cenario">
    <div class="predio">
        <div class="janela"></div><div class="janela"></div><div class="janela"></div>
        <div class="janela"></div><div class="janela"></div><div class="janela"></div>
        <div class="janela"></div><div class="janela"></div><div class="janela"></div>
        <div class="janela"></div><div class="janela"></div><div class="janela"></div>
    </div>
    <div class="chao"></div>

    <div id="aranha" onclick="iniciarAnimacao()">
        <div class="cabeca-aranha">
            <div id="olho1" class="olho esq"></div>
            <div id="olho2" class="olho dir"></div>
        </div>
        <div class="corpo-aranha"></div>
    </div>

    <div id="kuromi">
        <div class="cabeca-k">
            <div class="orelha-k esq"></div>
            <div class="orelha-k dir"></div>
            <div class="caveira"></div>
            <div class="olho-k esq"></div>
            <div class="olho-k dir"></div>
        </div>
        <div class="corpo-k"></div>
    </div>

    <div id="coracao">❤️</div>
    <div id="balao">Te amo rafa ❤️</div>
</div>

<script>
    let animado = false;
    function iniciarAnimacao() {
        if (animado) return;
        animado = true;

        const aranha = document.getElementById('aranha');
        const kuromi = document.getElementById('kuromi');
        const olho1 = document.getElementById('olho1');
        const olho2 = document.getElementById('olho2');
        const coracao = document.getElementById('coracao');
        const balao = document.getElementById('balao');

        // 1. Homem-Aranha cai
        aranha.style.top = '400px';

        // 2. Chega ao chão e fica com os olhos "X" (desmaiado)
        setTimeout(() => {
            olho1.className = "olho morto";
            olho1.innerHTML = "X";
            olho2.className = "olho morto";
            olho2.innerHTML = "X";
            olho2.style.left = "20px";
        }, 1200);

        // 3. Kuromi anda até ele
        setTimeout(() => {
            kuromi.style.right = '375px';
        }, 1500);

        // 4. Beijo (Coração aparece)
        setTimeout(() => {
            coracao.style.display = 'block';
        }, 2800);

        // 5. Ressuscita, olhos voltam ao normal e mostra o balão "Te amo rafa"
        setTimeout(() => {
            coracao.style.display = 'none';
            olho1.className = "olho esq";
            olho1.innerHTML = "";
            olho2.className = "olho dir";
            olho2.innerHTML = "";
            olho2.style.left = "";
            balao.style.display = 'block';
        }, 4200);
    }
</script>

</body>
</html>
"""

# Renderiza o HTML no Streamlit
components.html(html_code, height=520)