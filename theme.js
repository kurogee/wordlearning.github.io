const theme_css = {
    "default_theme" : {
        "path" : "default_theme.css",
        "need_level" : 0
    },

    "gaming_theme" : {
        "path" : "black_theme.css",
        "need_level" : 5
    },
}

function change_theme(parent_path, theme_name) {
    let theme = theme_css[theme_name];
    let theme_path = parent_path + theme["path"];
    let theme_need_level = theme["need_level"];
    let user_level = get_user_level();

    if (user_level >= theme_need_level) {
        let link = $("head link[rel='stylesheet']")[0];
        link.href = theme_path;
    }
}