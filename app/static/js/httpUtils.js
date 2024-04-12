/**
 * http 请求工具
 * {
 * ok: boolean 是否成功
 * msg: string 错误信息
 * data: object 具体的数据
 * }
 */

(function (win) {
    function ok(data) {
        return {
            ok: true,
            data
        }
    }

    function error(msg) {
        return {ok: false, msg}
    }

    function doHttp(method, url, params, dataType = '') {
        return new Promise((resolve, reject) => {
            let opts = {
                url: url,
                type: method,
                data: params,
                success: function (data) {
                    resolve(ok(data))
                },
                error: function () {
                    resolve(error(`${url} ${method} 请求出错!`))
                }
            }
            if (dataType === 'json') {
                opts.dataType = dataType
                opts.data = JSON.stringify(params)
                opts.contentType = "application/json; charset=utf-8"
            }
            console.log(opts)
            $.ajax(opts);
        })

    }

    win.httpKit = {
        doGet(url, params) {
            return doHttp('get', url, params)
        },
        doPost(url, params) {
            return doHttp('post', url, params, 'json')
        }
    }
})(window)

