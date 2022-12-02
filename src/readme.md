# image-process 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=image-process&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=image-process" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=image-process&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=image-process" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=image-process&type=packageDownload">
  </a>
</p>

<description>

> ***图片处理功能***

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |      
| --- |  --- |   
| 权限/策略 | AliyunFCFullAccess |  

</table>

<codepre id="codepre">

# 代码 & 预览

- [ :smiley_cat:  源代码](https://github.com/devsapp/image-process)

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=image-process) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=image-process)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init image-process -d image-process`   
    - 进入项目，并进行项目部署：`cd image-process && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情

使用python [wand](https://docs.wand-py.org/en/0.5.6/index.html)图片处理库进行常见的图片处理：

| 功能   | 请求路径      | 参数                                                    |   
|------|-----------|-------------------------------------------------------|  
| 拼接   | /pinjie   | left=bucket/image1.jpg&right=bucket/image2.jpg        |    
| 水印   | /watermark | img=bucket/image.jpg&text=hello-fc                    |    
| 格式转换 | /format   | img=bucket/image.jpg&fmt=png                          |    
| 图片转灰 | /gray | img=bucket/image.jpg(or .png,jpeg,webp)               |
| 保存结果 | 上述参数均可    | img=bucket/image.jpg&fmt=png&target=bucket/output.png |    

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>
