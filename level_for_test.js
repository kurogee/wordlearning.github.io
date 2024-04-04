// レベルを付けて、学習者のモチベーションを高める

// レベルの初期設定
// localStorageに保存されていない場合は、初期値を設定する
window.addEventListener('load', function () {
    if (!localStorage.getItem('level')) {
        localStorage.setItem('level', 1);
        localStorage.setItem('exp', 0);
    }
});

function showLevel() {
    // 経験値・レベルの表示
    let now_bar = $("#now_bar");
    let other_bar = $("#other_bar");

    now_bar.css("width", "0%");
    other_bar.css("width", "100%");

    document.getElementById("exp").textContent = "経験値：" + level.getLevel().exp + '/' + level.getNeedExp();
    document.getElementById("level").textContent = "Lv. " + level.getLevel().level;

    // アニメーションでバーを動かす
    now_bar.animate({ width: parseInt(localStorage.getItem('exp')) / level.getNeedExp() * 100 + '%' }, 1000);
    other_bar.animate({ width: 100 - (parseInt(localStorage.getItem('exp')) / level.getNeedExp() * 100) + '%' }, 1000);
}

// レベル管理のための関数をまとめたオブジェクト
let level = {
    // 経験値を加算する
    addExp: function (value) {
        const sound = new Audio('../sounds/charge.mp3');
        sound.volume = 0.4;
        let exp = parseInt(localStorage.getItem('exp'));
        let newExp = exp + value;
        if (newExp >= this.getNeedExp()) {
            let remain = newExp - this.getNeedExp();
            this.levelUp();
            localStorage.setItem('exp', remain);
        } else {
            localStorage.setItem('exp', newExp);
            setTimeout(function () {
                sound.play();
            }, 1000);
        }
    },
    // レベルアップする
    levelUp: function (remain) {
        const levelup_sound = new Audio('../sounds/levelUP!.mp3');
        levelup_sound.volume = 0.7;
        let level = parseInt(localStorage.getItem('level'));
        level++;
        localStorage.setItem('level', level);
        // 経験値をリセット、経験値が余る場合は次のレベルに持ち越す
        localStorage.setItem('exp', remain);

        // レベルアップの演出を表示
        setTimeout(function () {
            levelup_sound.play();
            $("#levelup_text").html("レベルアップ！");
            $("#levelup_text").css('color', 'red');
            setTimeout(function () {
                $("#levelup_text").html("");
                $("#bar").css('color', 'black');
            }, 3000);
        }, 1000);
    },
    // レベルアップの判定
    getNeedExp: function () {
        return parseInt(localStorage.getItem('level')) * 100;
    },
    // レベル、経験値を更新する
    reloadLevel: function () {
        // jqueryで経験値のバーにアニメーションをつける
        // now_barとother_barは一緒に動かす
        let now_bar = $("#now_bar");
        let other_bar = $("#other_bar");

        // レベルアップ時は端まで行ってから0に戻る
        let width_to_percent = now_bar.width() / now_bar.parent().width() * 100;
        let exp_to_percent = this.getLevel().exp / this.getNeedExp() * 100;
        console.log(width_to_percent);
        console.log(exp_to_percent);
        if (exp_to_percent < width_to_percent) {
            now_bar.animate({ width: "100%" }, 1000);
            other_bar.animate({ width: '0%' }, 1000);
            // アニメーションが終わったら、一旦経験値を0に戻す
            let exp = this.getLevel().exp;
            let need_exp = this.getNeedExp();
            setTimeout(function () {
                now_bar.stop();
                other_bar.stop();
            
                now_bar.css('width', '0%');
                other_bar.css('width', '100%');
        
                // ここで新しいアニメーションを開始
                now_bar.animate({ width: exp / need_exp * 100 + '%' }, 1000);
                other_bar.animate({ width: 100 - (exp / need_exp * 100) + '%' }, 1000);
            }, 1000);
        } else {
            now_bar.animate({ width: this.getLevel().exp / this.getNeedExp() * 100 + '%' }, 1000);
            other_bar.animate({ width: 100 - (this.getLevel().exp / this.getNeedExp() * 100) + '%' }, 1000);
        }

        document.getElementById("exp").textContent = "経験値：" + this.getLevel().exp + '/' + this.getNeedExp();
        document.getElementById("level").textContent = "Lv. " + this.getLevel().level;
    },
    getLevel: function () {
        return {
            level: parseInt(localStorage.getItem('level')),
            exp: parseInt(localStorage.getItem('exp'))
        };
    }
};