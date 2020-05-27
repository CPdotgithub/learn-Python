# requests 中的  text 和 content
    response.text 
    类型：str 
    解码类型：根据HTTP头部对响应的编码做出有根据的推测，推测的文本编码 
    如何修改编码方式：response.encoding=”gbk”

    response.content 
    类型：bytes 
    解码类型：没有指定 
    如何修改编码方式：response.content.decode(“utf8”)

    两者区别在于，content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。

    直接输出content，会发现前面存在b’这样的标志，这是字节字符串的标志，而text是，没有前面的b,对于纯ascii码，这两个可以说一模一样，对于其他的文字，需要正确编码才能正常显示。大部分情况建议使用.text，因为显示的是汉字，但有时会显示乱码，这时需要用.content.decode(‘utf-8’)，中文常用utf-8和GBK，GB2312等。这样可以手工选择文字编码方式。

    所以简而言之，.text是现成的字符串，.content是字节码还要编码，但是.text不是所有时候显示都正常，这是就需要用.content进行手动编码。
