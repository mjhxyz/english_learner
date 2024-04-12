/**
 * 工具
 */
(function (win) {
    win.utils = {
        /**
         * 打开新的弹出窗口
         * @param title
         * @param url
         * @param callback
         * @param width
         * @param height
         */
        openDialog(title, url, callback, width = '680px', height = '520px') {
            layer.open({
                type: 2,
                title: title,
                area: [width, height],
                content: url,
                fixed: false, // 不固定
                // maxmin: true,
                shadeClose: true,
                btn: ['确定', '取消'],
                btnAlign: 'c',
                yes: function (index, layero) {
                    let iframeWin = window[layero.find('iframe')[0]['name']];
                    // var elemMark = iframeWin.$('#mark'); // 获得 iframe 中某个输入框元素
                    callback(index, layero, iframeWin)
                    // // 获取 iframe 的窗口对象

                    // var value = elemMark.val();
                    //
                    // if ($.trim(value) === '') return elemMark.focus();
                    // // 显示获得的值
                    // layer.msg('获得 iframe 中的输入框标记值：' + value);
                }
            });
        }
    }

})(window)