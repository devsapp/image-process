
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# image-process-dipper 帮助文档

<description>

本案例将 Wand，这一功能强大、易于使用的Python图像处理库，快速搭建并部署到阿里云函数计算 FC。

</description>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  | 相关文档 |
| --- |  --- | --- |
| 函数计算 |  AliyunFCFullAccess | [帮助文档](https://help.aliyun.com/product/2508973.html) [计费文档](https://help.aliyun.com/document_detail/2512928.html) |
| 日志服务 |  AliyunFCServerlessDevsRolePolicy | [帮助文档](https://help.aliyun.com/zh/sls) [计费文档](https://help.aliyun.com/zh/sls/product-overview/billing) |

</service>

<remark>



</remark>

<disclaimers>



</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [云原生应用开发平台 CAP](https://devs.console.aliyun.com/applications/create?template=image-process-dipper) ，[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://devs.console.aliyun.com/applications/create?template=image-process-dipper) 该应用。
   
</appcenter>
<deploy>
    
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

本案例将 Wand，这一功能强大、易于使用的Python图像处理库，快速搭建并部署到阿里云函数计算 FC。

Wand 提供了一个简单的API来创建、读取、保存、编辑和显示图像。这个库在执行复杂的图像操作时能够保持较高的性能，并且在Windows、Linux、macOS和其他支持Python的平台上都能运行。Wand支持多种常见的图像文件格式，包括JPEG、PNG、GIF等，并提供了便捷的方法来读取和保存这些格式的文件。

Wand的图像处理功能丰富，包括修剪、缩放、旋转、合并等基本操作，以及滤镜、调整亮度、对比度等高级功能。这使得开发者能够轻松实现各种图像处理需求。

通过云原生应用开发平台，您只需要几步，就可以体验 wand 图片处理库 ，并享受 Serverless 架构带来的降本提效的技术红利。

</appdetail>

## 使用流程

<usedetail id="flushContent">

### 查看部署的案例

部署完成之后，您可以看到系统返回给您的案例地址，点开url，就可以看到图片处理首页：

![](https://img.alicdn.com/imgextra/i1/O1CN019J0wHL1i0LpODWgIf_!!6000000004350-0-tps-2868-1554.jpg)

在对象存储oss中上传存储图片，从oss中获取目标图片，如：rockuw-sh/图片名

根据不同的请求路径，使用python [wand](https://docs.wand-py.org/en/0.5.6/index.html)图片处理库进行常见的图片处理：

| 功能   | 请求路径      | 参数                                                    |   
|------|-----------|-------------------------------------------------------|  
| 拼接   | /pinjie   | left=bucket/image1.jpg&right=bucket/image2.jpg        |    
| 水印   | /watermark | img=bucket/image.jpg&text=hello-fc                    |    
| 格式转换 | /format   | img=bucket/image.jpg&fmt=png                          |    
| 图片转灰 | /gray | img=bucket/image.jpg(or .png,jpeg,webp)               |
| 保存结果 | 上述参数均可    | img=bucket/image.jpg&fmt=png&target=bucket/output.png |

</usedetail>

## 注意事项

<matters id="flushContent">
</matters>
