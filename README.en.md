# AutoPWN

#### Description
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
 

#### Software Architecture
Software architecture description

#### Installation

1.  xxxx
2.  xxxx
3.  xxxx

#### Instructions

1.  xxxx
2.  xxxx
3.  xxxx

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request


#### Gitee Feature

1.  You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2.  Gitee blog [blog.gitee.com](https://blog.gitee.com)
3.  Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4.  The most valuable open source project [GVP](https://gitee.com/gvp)
5.  The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6.  The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
