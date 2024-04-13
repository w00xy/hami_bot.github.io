<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" 
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"/>
    <title>HAPI</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="reset.css">
</head>
<body>
    <div class="visible_main_screen" id="main_screen">
        <div class="name_qr">
            <img src="assets/logo.png" class="name">
            <a href="#"><img src="assets/qr.jpg" class="qr"></a>
        </div>
        <div class="center">
            <div class="left_el">
                <div>
                    <img src="assets/img_tocen.png">
                    <h1>HAMI Balance</h1>
                    <h2>0.0042344</h2>
                </div>
            </div>
            <div class="right_el">
                <div class="right_el_one" onclick="getStorage()">
                    <div class="right_el_one_top">
                        <div class="right_el_one_txt">
                            <h2>Storage</h2>
                            <h1>Mining</h1>
                        </div>
                        <img src="assets/chest.png" class="chest_img">
                    </div>
                    <div class="right_el_one_bottom">
                        <p class="claim_count">0.03232</p>
                        <div class="claim_bar"></div>    
                    </div>
                </div>
                <div class="right_el_two">
                    <div class="right_el_two_top">
                        <div class="right_el_two_txt">
                            <h2>Research</h2>
                            <h1>Boosters</h1>
                        </div>
                        <img src="assets/research.webp" class="study_img">
                    </div>
                    <div class="btn_claim">
                        <h2>Study</h2>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer">
            <h2 class="name_block">Coins</h2>
            <div class="ftr_el">
                <img src="assets/mini_toc.png">
                <div>
                    <h2 style="margin-left: 8px;">HAMI</h2>
                    <p class="ftr_el_txt">0 / $0</p>
                </div>
                <p class="ftr_el_txt_right">0</p>
            </div>
            <div class="ftr_el">
                <img src="assets/ton_symbol.png">
                <div>
                    <h2 style="margin-left: 8px;">TON</h2>
                    <p class="ftr_el_txt">0 / $7.20</p>
                </div>
                <p class="ftr_el_txt_right">$0.00</p>
            </div>
        </div>
    </div>
    <!-- storage_screen -->
    <div class="hide" id="storage_screen">
        <div class="top_txt">
            <p class="s2ttp1">In storage:</p>
            <div class="s2ttg1">
                <img src="assets/mini_toc.png" class="">
                <p>0.0042344</p>                
            </div>
            <div class="s2ttg2">
                <p>HAMI Balance:</p>
                <img src="assets/logo_toc_no_shadow.png">
                <p>1.123245</p>
            </div>
        </div>
        <img src="assets/hami.gif" class="gif_hami">
        <div class="claim_rec">
            <div class="claim_content">
                <img src="assets/chest_rev.png" class="s2ccimg">
                <div class="claim_content_center">
                    <p class="s2cccp1">Storage</p>
                    <div class="s2cccg1">
                        <img src="assets/clock.png">
                        <p>3h 37'm to fill</p>
                    </div>
                    <div class="s2cccg2">
                        <img src="assets/logo_toc_no_shadow.png">
                        <p>0.03 HAMI/hour</p>
                    </div>
                </div>
                <div class="claim_content_right">Collect</div>
            </div>
            <div class="s2cr_full_bar">
                <div class="s2cr_farm_bar"></div>
            </div>
        </div>
        <div class="s2_btn_rec">
            <a href="#">
                <img src="assets/farm.png">
                <p>Farm</p>
            </a>
            <div class="s2_btn_rec_line"></div>
            <a href="#">
                <img src="assets/boost.webp">
                <p>Boosts</p>
            </a>
            <div class="s2_btn_rec_line"></div>
            <a href="#">
                <img src="assets/storage.webp">
                <p>Storage</p>
            </a>
            <div class="s2_btn_rec_line"></div>
            <a href="#">
                <img src="assets/events.webp">
                <p>Events</p>
            </a>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>