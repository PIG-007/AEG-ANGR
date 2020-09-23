# AutoPWN

#### 介绍
# 开发文档

目前版本：beta v0.1

## 漏洞检测

主要使用的工具是Angr

### Stack Overflow and Head Overflow

针对栈溢出，主要原理是检测EIP或者RIP的值是否





#### 例子： insomnihack_aeg - demo_bin

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char component_name[128] = {0};

typedef struct component 
{
    char name[32];
    int (*do_something)(int arg);
} comp_t;

int sample_func(int x) 
{
    printf(" - %s - recieved argument %d\n", component_name, x);
}

comp_t *initialize_component(char *cmp_name) {
    int i = 0;
 

#### 软件架构
软件架构说明


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
