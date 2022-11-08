# 深入浅出Windows驱动开发——学习笔记

## 1 基本介绍

    操作系统刚出现的时候是由机器语言和汇编语言编写的，为了可移植性等采用了C语言。C语言完全可以开发出所有的驱动程序，但对于微软提供的WDF驱动开发模型，C++是最好的选择。
    驱动程序编译成的二进制文件是SYS类型文件，和普通的EXE类型文件，都是PE(Portable Executable File Format)的格式，是微软Windows平台环境下主流的可执行程序标准格式，DLL也是其中之一。微软提供的内核编程接口和实例只有C/C++的。
    驱动程序的开发和普通应用程序的开发在分析需求、设计、编码、调试、测试、发布、维护的流程基本一致，但是后面几个环节有较大的区别。

```C
#include <NTDDK.h> 
NTSTATUS
DriverEntry (
    __in PDRIVER_OBJECT DriverObject,
    __in PUNICODE_STRING RegistryPath
    )
{
    DbgPrint("Hello, Windows Driver!");
    return STATUS_SUCCESS;
}
```

    代码讲解:
    头文件NTDDK.h是NT驱动必须包含的一个头文件，WDM驱动需要换成WDM.h
    整段代码只有一个DriverEntry函数，这个函数是所有驱动程序的入口函数，类似于Win32编程下的WinMain函数或C语言的main函数
    函数的两个参数，分别代表驱动对象的指针和注册表子键的字符串指针。__in是一个宏，代表这个参数是入口参数，相反有出口参数__out
    函数内，DbgPrint是一个函数，类似于C语言的printf函数，打印一串字符串。STATUS_SUCCESS是一个宏。打印的内容无法通过控制台查看，需要借助其他工具。
    开发环境是微软提供的WDK。

```C

#ifndef __HELLODRIVER_H__
#define __HELLODRIVER_H__

#include <NTDDK.h>

typedef struct _DEVICE_EXTENSION {

    PDEVICE_OBJECT DeviceObject;    // 指回设备对象的指针 
    UNICODE_STRING DeviceName;      // 设备名称 
    UNICODE_STRING SymbolicLink;    // 符号链接名 
          
}DEVICE_EXTENSION, *PDEVICE_EXTENSION;

NTSTATUS
DriverEntry (
    __in PDRIVER_OBJECT DriverObject,
    __in PUNICODE_STRING RegistryPath
    );

VOID
DriverUnload (
    __in PDRIVER_OBJECT DriverObject
    );
    
NTSTATUS
DefaultDispatch (
    __in PDEVICE_OBJECT DeviceObject,
    __in PIRP Irp
    );

#endif  // End of __HELLODRIVER_H__ 
```

```C

#include "HelloDRIVER.h" 

//*============================================================================ 
//*= = 预处理定义 
//*============================================================================ 

#pragma alloc_text(INIT, DriverEntry)
#pragma alloc_text(PAGE, DefaultDispatch)
#pragma alloc_text(PAGE, DriverUnload)

//*============================================================================
//*= = 函数名称:DriverEntry
//*= = 功能描述:驱动程序入口函数 
//*= = 入口参数:PDRIVER_OBJECT, PUNICODE_STRING 
//*= = 出口参数:NTSTATUS
//*============================================================================

NTSTATUS
DriverEntry (
    __in PDRIVER_OBJECT DriverObject,
    __in PUNICODE_STRING RegistryPath
    )
{
    NTSTATUS status;
    PDEVICE_OBJECT deviceObject;
    PDEVICE_EXTENSION deviceExtension;
    UNICODE_STRING symbolicLink;
    UNICODE_STRING deviceName;
    ULONG i;
    KdPrint(("Enter HelloDRIVER DriverEntry!\n"));
    
    UNREFERENCED_PARAMETER(RegistryPath); 
    
    RtlInitUnicodeString(&deviceName, L"\\Device\\HelloDRIVER");

    // 处理派遣例程 
    for (i = 0; i <= IRP_MJ_MAXIMUM_FUNCTION; i++)
    {
        DriverObject->MajorFunction[i] = DefaultDispatch; 
    }
    
    DriverObject->DriverUnload = DriverUnload;
    DriverObject->MajorFunction[IRP_MJ_CREATE] = DefaultDispatch; 
    DriverObject->MajorFunction[IRP_MJ_CLOSE] = DefaultDispatch; 
    DriverObject->MajorFunction[IRP_MJ_READ] = DefaultDispatch; 
    DriverObject->MajorFunction[IRP_MJ_WRITE] = DefaultDispatch; 
    
    // 创建设备 
    status = IoCreateDevice( DriverObject,
                             sizeof(DEVICE_EXTENSION),
                             &deviceName,
                             FILE_DEVICE_UNKNOWN,
                             0,
                             TRUE,
                             &deviceObject);
    if(!NT_SUCCESS(status))
    {
        return status;
    }
    
    deviceObject->Flags = DO_BUFFERED_IO;
    deviceExtension = (PDEVICE_EXTENSION)deviceObject->DeviceExtension;
    deviceExtension->DeviceObject = deviceObject;
    deviceExtension->DeviceName = deviceName;
    
    RtlInitUnicodeString(&symbolicLink, L"\\??\\HelloDRIVER");
    deviceExtension->SymbolicLink = symbolicLink;
    
    // 创建符号链接 
    status = IoCreateSymbolicLink(&symbolicLink, &deviceName);
    
    if(!NT_SUCCESS(status))
    {
        IoDeleteDevice(deviceObject);
        return status;
    }
    
    KdPrint(("End of HelloDRIVER DriverEntry!\n")); 
    return status;
}

//*============================================================================
//*= = 函数名称:DriverUnload 
//*= = 功能描述:驱动程序卸载函数 
//*= = 入口参数:PDRIVER_OBJECT 
//*= = 出口参数:VOID 
//*============================================================================

VOID
DriverUnload (
    __in PDRIVER_OBJECT DriverObject
    )
{
    PDEVICE_OBJECT deviceObject;
    UNICODE_STRING linkName;
    KdPrint(("Enter HelloDRIVER DriverUnload!\n"));
    
    deviceObject = DriverObject->DeviceObject;
    
    while(NULL != deviceObject)
    {
        PDEVICE_EXTENSION deviceExtesion = 
                   (PDEVICE_EXTENSION)deviceObject->DeviceExtension;
        
        // 删除符号链接与设备
        linkName = deviceExtesion->SymbolicLink;
        IoDeleteSymbolicLink(&linkName);
        deviceObject = deviceObject->NextDevice;
        IoDeleteDevice(deviceExtesion->DeviceObject);
    }
    
    KdPrint(("End of HelloDRIVER DriverUnload!\n"));
}

//*============================================================================
//*= = 函数名称:DefaultDispatch 
//*= = 功能描述:驱动程序默认派遣例程 
//*= = 入口参数:PDEVICE_OBJECT, PIRP 
//*= = 出口参数:NTSTATUS
//*============================================================================

NTSTATUS
DefaultDispatch (
    __in PDEVICE_OBJECT DeviceObject,
    __in PIRP Irp
    )
{
    NTSTATUS status;
    KdPrint(("Enter HelloDRIVER DefaultDispatch!\n"));
    
    UNREFERENCED_PARAMETER(DeviceObject);
    status = STATUS_SUCCESS;
    
    // 完成IRP请求 
    Irp->IoStatus.Status = status;
    Irp->IoStatus.Information = 0;
    IoCompleteRequest(Irp, IO_NO_INCREMENT);
    
    KdPrint(("End of HelloDRIVER DefaultDispatch!\n"));
    return status;
}

```

    代码讲解
    ifdef和ifndef是C语言中常见的预处理，用来避免头文件重复包含导致编译错误，#pragma once也能避免这个错误，但是可移植性稍差。
    #pragma alloc_text(INIT, DriverEntry)，预处理，在驱动开发中，需要为每一个函数指定其是分页内存还是非分页内存。INIT标识是指此函数在驱动加载时使用，是初始化相关的函数，驱动成功加载以后可以从内存卸载。PAGE标识是指此函数在驱动运行时可以被交换到磁盘上。如果不指定，编译器默认为非分页内存。
    一般情况下，不需要考虑这些问题，但是有些特殊情况，代码是不允许被交换到磁盘上的，否则将导致操作系统蓝屏或自动重启。函数声明必须在这些指定内存分配的预处理之前，否则无法通过编译(函数必须先声明，然后才可用于pragma列表)
    DriverEntry是驱动程序的入口函数，由操作系统内核中的I/O管理器调用。
    KdPrint也是一个字符串打印函数，和DbgPrint是同一个函数，是它的宏定义方式，用以打印调试信息。将其定义为宏的好处在于调试版本打印出具体信息供开发者参考，而在发行版本编译时完全被移除，从而减小驱动文件大小并有助于提高程序的运行效率。
    在应用程序中调试版本和发行版本分别被称为Debug版本和Release版本，而在驱动程序中则被称为Check版本和Free版本。调试版本包含大量调试信息，没有经过优化，方便开发者寻找程序缺陷和漏洞。
    UNREFERENCED_PARAMETER是一个宏，经常被用来指定参数未被引用，可以避免不必要的警告。
    除非十分确定警告不会对驱动程序带来不稳定的因素，否则请修正，因为驱动程序的崩溃会导致操作系统的崩溃，直接造成死机或蓝屏。
    RtlInitUnicodeString(&deviceName, L"\\Device\\HelloDRIVER")，对一个Unicode字符串进行初始化。Windows内核中大量使用Unicode字符串，其具体操作有一系列函数，这一系列函数属于Rtl系列，也就是微软推荐使用的运行时函数。
    for (i = 0; i <= IRP_MJ_MAXIMUM_FUNCTION; i++)，宏IRP_MJ_MAXIMUM_FUNCTION代表驱动程序最大的派遣函数指针数，DriverObject->MajorFunction[i] = DefaultDispatch;用一个默认的派遣函数来初始化。
    这些派遣函数又可以称为回调函数，由定义实现，提供给操作系统调用。回调函数在驱动程序中是主要的工作重点。
    对于普通的驱动程序，可以不考虑对所有的派遣函数指针进行初始化，但是如果想要实现一个过滤驱动程序，需要参照上述方式初始化。如果没有进行全部初始化，编译器会对未处理的派遣函数指针进行默认处理。
    卸载函数DriverUnload，这个派遣函数必须单独提供，并且在操作系统版本不同的情况下，这个函数可能需要注意一些不同的东西。如果不打算对驱动程序进行卸载，这个函数可以不用提供。
    IRP_MJ_CREATE、IRP_MJ_CREATE、IRP_MJ_READ、IRP_MJ_WRITE，对应操作系统的创建、关闭以及读写的派遣函数。还有其他的派遣函数需要提供。
    status = IoCreateDevice( DriverObject,sizeof(DEVICE_EXTENSION),&deviceName,FILE_DEVICE_UNKNOWN,0,TRUE,&deviceObject)，使用IoCreateDevice函数宏创建一个设备对象，该设备类型为"FILE_DEVICE_UNKNOWN"，是一种独占设备，在运行时只能被一个应用程序所使用。判断设备是否创建成功，并进行必要的失败处理，驱动程序中这样的处理对于驱动程序的健壮性起着不容忽视的作用。
    设置设备的标识，由BUFFERED_IO和DO_DIRECT_IO两种，代表了两种不同的缓冲区处理方式。
    status = IoCreateSymbolicLink(&symbolicLink, &deviceName)，使用IoCreateSymbolicLink函数宏创建了设备符号链接，并对创建结果判断以进行必要的失败处理。这个符号链接名主要用来与应用程序进行通信。如果创建失败，则删除已经创建的设备对象。
    驱动程序的设备名称对应用程序是透明的，所以只能用于内核程序，这也是为什么要创建设备符号链接的原因。
    DriverUnload函数，功能是删除设备对象和设备符号链接，如果在DriverEntry函数中分配了资源，也要在这释放。
    DefaultDispatch函数，具体实现是直接完成了IRP(Input/Output Request Package，输入输出请求包)
    IoCompleteRequest(Irp, IO_NO_INCREMENT)，直接完成IRP

## 2 商业驱动开发技术

    Windbg是一个较好的调试方法。

### 2.2 64位驱动开发技术

    64位驱动编写技术
        64位操作系统目录部署，为了保持应用程序的兼容性，以及减少应用程序从Win32移植到64位系统的开销，系统的目录名保持不变。因此，\WINDOWS\system32目录中存储的是本地64位程序。因为WOW64要钩住所有的系统调用，所以它转换了所有路径相关的APIs，并将路径名\WINDOWS\system32替换为\WINDOWS\system32\SysWOW64。WOW64还将\WINDOWS\system32\IME重定位到\WINDOWS\system32\IME(x86)，以帮助32位应用程序兼容于64位系统。32位程序被装载到\Program Files(x86)目录下，而64位程序则被正常装载到正常的\Program Files目录下。
        少数目录因为兼容性要求的原因而没有被重定位，使得32位应用程序访问到的是原始目录位置。这些目录包括%windir%\system32\下的drivers\etc、spool、catroot2、logfiles
        WOW64提供了一种禁用文件重定位的机制，线程可以调用函数Wow64EnableWow64FsRedirection。该机制在Windows Server 2003及以后的版本中有效
        程序目录，32位Program Files(x86) 所有的32位程序，64位Program Files
        系统目录，64位system32，32位SysWOW64;在32位程序运行时，如果不特意处理，访问system32目录时，会被WOW64层自动重定向到SysWOW64目录
        数据类型，在64位环境下，所有的指针、句柄都是64位。DWORD(无符号整数)、INT、LONG、UINT、ULONG都有32和64位的。
        当需要数据类型的精度随着处理器位数大小变化时，使用指针精度数据类型，又称为多态数据类型。通常以_PTR后缀结尾，DWORD、HALF(指针大小的一般，用于包含一个指针和两个小型字段的结构)、INT、LONG、SIZE(指针可以引用的最大字节数，用于必须跨指针的整个范围的计数)、SSIZE(有符号SIZE)、UHALF、UINT、ULONG、LPARAM、WPARAM。在需要使用数据保存指针或句柄时，请尽量使用同类型变量，如果因为程序原因不能使用同类型变量时，请使用指针精度变量。
    32位应用程序与64位驱动混合模式
        驱动要支持32位IOCTL
            某些IOCTL可能包含有指针的结构，所以要特别小心，必须根据被调用者解析结构或者输出结构。三种解决办法，1避免使用IOCTL传递包含有指针的结构，2通过API IOIs32bitProcess()来判断上层调用者的程序类型，3在64位程序中采用新的IOCTL命令。
        使用固定精度的数据类型代替指针精度的数据类型
            为了解决因为数据类型导致的32位和64位数据长度不一致的问题，可以采用固定精度的数据类型来代替指针精度的数据类型处理数据
        避免固定精度的数据类型对不齐
            在32位和64位混合编程中，会发生数据长度一致，但是对齐长度不一样的情况。不是所有的IOCTL/FSCTL缓冲对不齐的问题都可以通过修改指针精度的数据类型位固定精度的数据类型而得到解决，这意味着内核模式驱动的IOCTL和FSCTL请求中传递的固定精度的数据类型或者指针精度的数据类型需要进行转换(thunked)，就是在不同长度或类型之间的转换。结构类型的固定精度会被影响，可以使用TYPE_ALIGNMENT宏知道指定数据类型在特定平台上的对齐长度。
            1避免缓冲区对不齐的安全方法就是在访问缓冲内容前进行拷贝操作
            2UNALIGNED宏告诉C编译器生成可以无故障存取的DeviceTime域的代码。但是在安腾平台上使用这个宏，会导致驱动程序体积变大。
            指针类型也会被影响。和基于METHOD_NEITHER的IOCTL和FSCTL一样，嵌入到缓冲型的I/O请求中的指针也是直接从应用层程序中传递到内核驱动中的，在这些指针上没有进行校验，在访问这些内嵌的指针之前，需要在一个try/catch块中调用ProbeForRead或ProbeForWrite进行缓冲区指针校验。

### 2.3 驱动程序的发布与测试

    在x86-64平台下，还需要考虑一个问题，数字签名和WHQL。
    程序驱动签名
        从Windows Vista开始，Windows系统要求应用程序和驱动程序需要签名以提高系统安全性。对于驱动程序来讲，从Windows Vista开始的64位平台上，驱动程序必须签名。普通应用程序的签名只需要可信根证书即可，即只需要将签名证书的根安装到信任根证书区域即可。
        驱动程序的签名，需要使用由VeriSign和GlobalSign签发的证书，其他机构签发的证书无效。原因是这两个机构是Windows根信任的，微软为这两个机构签发了根证书的信任证书，根据PKI机制的传递性，由这两个信任根签发的最终用户证书将受到微软的信任。这种信任是严格的，不会因为用户的操作而改变，即使将自己生成的根证书安装到受信任的根证书区域，也无济于事。
        签名的原理，权威机构会给用户签发一份最终的签名证书，证书包括:用户的公私钥对、基于RSA算法，用户的证书信息、包括用户名称和类型等，上一级CA对本证书的签名信息。
        将要签名的文件通过Hash算法进行信息摘要，对整个文件的Hash结果，再通过RSA的私钥进行加密，并将加密后的结果和相关信息写入文件尾部。写入的信息包括:证书信息、加密后的结果等。
        在验证时，需要取出尾部的证书相关信息，通过证书自带的公钥解开签名信息，查对原始文件生成的Hash值是否跟签名相符，如果相符，即认为正确签名了。在签证时，要先验证文件中用户证书是否有效，然后再用用户证书中的公钥解开签名结果进行比较。用户证书的验证过程:1使用用户证书中自带的相关信息验证证书完整性，确保证书由上一级CA机构签发，并且没有经过修改;2验证上一级CA证书由更上一级CA证书签名，验证过程同文件签名验证过程;3直到发现本级CA证书由自己签发为止，这就是根CA证书的自验证
        实际使用证书进行签名时，可以使用WDK自带的signtools.exe工具。
            signtool.exe sign /v /ac MSCV-VSClass3.cer /s "my" /n "MyCertName" /t http://timestamp.verisign.com/scripts/timestamp/dll %l
                MSCV-VSClass3.cer，VeriSign根证书的签名证书，由微软提供
                MyCertName是使用的签名证书名称，即证书的CommonName
                %l为要签名的驱动程序的全路径
        如果需要签名的程序带Inf文件，那么在使用上比较复杂，具体可以查看WDK自带的Inf2Cat工具的使用帮助。
        如果仅在测试模式下使用，操作系统不再检查根证书的信任关系，不过仅限于在驱动程序测试阶段使用。请不要在未经用户允许的情况下修改用户机器的工作模式。签名是为了操作系统和用户数据的安全，如果随意修改用户机器配置，使其工作于测试模式，将是非常危险的行为
    驱动程序测试
        驱动程序开发完成后，需要进行一些功能性测试，以保证它工作于最佳状态。通常需要进行以下测试
        内存使用测试
            内存使用测试的目的是查看驱动程序有没有发生内存分配失败的情况。可以使用操作系统的自带的Verifier工具进行测试，启动方式是直接在操作系统的命令行状态下运行Verifier。启动后设置为创建自定义设置。
            打开内存测试程序，可以提高故障查找能力。比如，由于驱动程序内存分配错误，将空的指针传递到下一层的驱动程序中而导致下一层的驱动程序蓝屏，Verifier程序打开后bug将会出现。
        功能测试
            功能测试通常使用黑盒测试技术，将驱动程序和应用程序连接好，让它在实际工作环境下运行，通过应用程序的反应来验证驱动程序功能是否符合设计文档的要求。在这种情况下没有其他好的办法，唯一可以借助的一些自动化测试工具，如WinRunner等，用来自动操作应用程序，模拟实际工作环境
        休眠测试
            将驱动程序正确安装到计算机后，打开休眠模式，让计算机在休眠后再被唤醒，确认驱动程序在休眠状态下可以正常工作。这对于硬件驱动程序来说，是验证电源管理功能的必要步骤。通常一次测试不足以发现故障现象，可以重复多次进行测试。
        长时间运行测试
            如果在常规的测试状态下无法发现问题，并不能说明驱动程序已经非常稳定了。此时需要配合应用程序，让驱动程序在实际工作环境或者接近于实际工作环境的情况下长时间运行，确保驱动程序的功能正常、稳定
    WHQL
        对于硬件驱动程序或者会产生Miniport设备的驱动程序来说，如果希望驱动程序更加稳定，符合Windows的严格要求，可以申请WHQL(Windows硬件设备质量实验室)测试

## WDF概述

    WDF(Windows Driver Framework, Windows驱动框架)是UMDF(User Mode Driver Framework, 用户模式驱动框架)和KMDF(Kernel Mode Driver Framework, 内核模式驱动框架)的总和。

### 3.1 主要特点

    WDF框架具有以下几个主要特点
        (1)系统兼容。由于框架内部磨合了系统、平台间的差异，而对外提供统一的DDI接口，从而使得使用WDF编写的驱动在跨平台、系统上表现非常优秀。
        (2)基于对象的框架。有一个最基本的对象，其他对象都基于这个对象进行扩展。而所有的WDF框架对象，一般又对应于某个标准的WDM驱动对象。最重要的对象包括:驱动、设备、IO请求、队列、目标对象等。
        (3)框架管理着所有对象的生命周期。它通过通用的引用计数，以及一套精心设计的父子层级关系来实现这个维护工作。
        (4)为框架对象所设计的一套设施，如上下文空间、同步锁等，使得框架对象极易操作，有安全性保障。
        (5)一套精心定义的PME(Property/Method/Event)编程接口。在WDK中看到的形如Wdfxxx的函数，都是WDF框架提供的编程接口，一般将其称为"框架DDI接口"
        (6)对WDM进行了完美封装，最大的突破在于实现了趋于完美的复杂的PNP与电源管理状态机(State Machine)。WDF驱动程序受益于此，只要提供非常简单的几个PNP与电源事件回调，就能实现完整功能。大多是时候，甚至根本就可以忽略他们，完全由框架代为处理。
        (7)处理IO请求更简便。通过使用框架IO请求对象(WDFREQUEST)能够轻松实现异步、同步处理，未完成请求的取消操作也极为方便。此外，又引入了IO队列概念，能够轻松实现多个IO请求的串行、并行和手动处理;并且IO队列还支持PNP和电源管理。

### 3.2 框架视图

![WDF内核框架](pic/WDF内核框架.png)

    用户程序:用户程序运行在用户层子系统中，内核对它来说是透明的，只能通过Win32API或更高级的用户层API来完成自己的工作。它与WDF内核驱动的交互，基本上是使用这几种API来实现:CreateFile与CloseHandle用于打开和关闭;ReadFile、WriteFile与DeviceIoControl用于进行IO操作。虽然在内核中WDF重新封装了驱动编程架构(WDM)，但用户程序对二者使用完全相同的编程方式
    内核子系统:内核子系统收到应用程序的请求后，将它包装成IRP并发送给正确的设备处理。内核子系统还要负责请求的完成后处理。
    WDF框架:WDF框架的内部实现，其实就是一个内核库形式的WDM驱动，并提供框架DDI接口给WDF驱动使用。框架内部实现了各种IRP命令的分发函数，这些内部分发函数就成为了WDF框架的上边沿和下边沿。从系统角度讲，所有驱动程序的上边沿负责接收IRP包，下边沿负责送出IRP包。这两件事，都是IRP分发函数要做的事情(不考虑文件驱动里面的Fast IO调用和总线驱动的接口调用，不通过IRP发送请求)
        WDF框架的最大价值，在于实现的三个重要模块:对象模块、IO模块和PNP/电源模块
    WDF驱动:一个纯粹的WDF驱动，可以完全利用WDF框架提供的DDI来完成任务。但内核服务并不对WDF驱动封闭，在必要的时候，WDF驱动还可以直接调用内核服务。在驱动的下边沿，在正常情况下，WDF驱动会让WDF框架帮助它将IO请求传递到下层驱动或设备;但在特殊情况下，WDF也可以直接获取IRP并自己将其传递到下层处理

### 3.3 兼容性

    能兼容WDM架构，是WDF的一个优点。

### 3.4 对象模型

    内核中的绝大多数称为对象者，都是结构体变量，例如DEVICE_OBJECT(设备对象)、DRIVER_OBJECT(驱动对象)等被称为内核对象，EPROCESS、KPROCESS等被称为执行体对象
    WDF中更广泛地使用了"对象"概念，WDF框架的对象成员包括:驱动、设备、内存、队列、IO请求、文件对象等。大部分框架对象都能够在WDM架构中找到对应物。
    WDF对象有共同的根。WDF_OBJECT对象中包含了基本信息:对象类型(Type)、对象长度(Len)、引用计数、指向Parent对象和子对象列表的指针等。Type和Len两个值用来区分各种不同类型的对象；引用计数用来维护对象的生命周期；指向Parent对象和子对象列表的指针，用来维护对象的集成关系，通过这种继承关系，WDF驱动中的所有框架对象共同构成一颗拥有唯一根对象(驱动对象)的对象树
    对象和句柄
        我们无法看到对象，只能看到句柄，一般是一个指针长度的索引(不同系统的位值不同)，指示它所代表的"对象指针"在一张表中的位值。
        从WDF.h头文件(可能是其他文件)中可以看到这些句柄的定义，WDFOBJECT是HANDLE的别名，而HANDLE等同于一个PVOID指针类型。struct WDFDRIVER__{int unused;}，unused不可使用，但是框架本身会进行使用。
    引用计数
        内核管理器维护全局内核对象的方法，为每个对象维护一个引用计数。每个内核对象都有一个对象头结构体，虽然是未文档化的，但可以用dt命令获取定义
        PointerCount是真正的引用计数，任何模块都不应该手动修改这个值，而应该使用ObReferenceObjectXXX系列函数增加一次引用，使用ObDereferenceObject函数减少一次引用。
        HandleCount应理解为句柄引用次数。由于内核对象既可以直接被内核程序使用(通过对象指针)，也可以间接地被用户程序使用(通过一个申请到的有效HANDLE)。所以PointerCount的值是内核引用和用户句柄引用的综合。HandleCount用来表现用户程序对内核对象的引用计数，用户程序每打开一次内核对象句柄，相应的Pointercount计数就增1，同时HandleCount计数也增加1；但如果内核程序直接通过ObReferenceObjectXXX函数增加引用计数，则只增加PointerCount计数而不影响HandleCount计数
        WDF框架对象并不是全局对象，所以轮不到对象管理器来管理，WDF框架必须自己提供管理逻辑。实现原则
            (1)WDF框架对象只能以句柄形式被引用，不能以指针形式被引用
            (2)每个框架对象只有唯一的句柄，这个句柄在创建时返回(WdfObjectCreate)，此时框架对象的引用计数为1。此后不能产生一个新句柄代表这个内核对象。每次的创建操作，对应一次删除操作(WdfObjectDelete)，删除将导致句柄失效，并减少一次引用计数。对象本身只有在引用计数降到0时才会被删除。WDF驱动程序总是应该保证:在调用WdfobjectDelete函数删除对象前，对象的引用计数已降为1
            (3)通过WdfObjectReferenceXXX函数增加框架对象的引用计数，通过WdfObjectDereferenceXXX函数减少框架对象的引用计数。调用WdfObjectDereferenceXXX函数后，如果框架对象的引用计数降为0，则框架对象被删除，其句柄失效
            代码分析
                WDFOBJECT Obj;
                WdfObjectCreate(WDF_NO_OBJECT_ATTRIBUTES, &Obj);//1
                WdfObjectReference(Obj);                        //2
                WdfObjectDelete(Obj);                           //3
                WdfObjectDereference(Obj);                      //4
                以上是错误的，句柄失效后再试图解除引用，会出现不可预料的结果。修改方法
                1删除第三行。驱动把删除的工作交给WDF框架来完成。在默认情况下，所有框架对象的根对象是DriverEntry函数中生成的驱动对象。驱动被卸载时，驱动对象会被删除，并附带将所有子对象都删除。但这种方法会带来运行时资源泄露，如果句柄Obj所代表的对象在第四行过后就不再被用到的话，驱动就应及时删除此对象以释放所占内存，否则这两个对象将一直存在，直到驱动卸载为止。
                2将3、4两行交换。
                3更加经典，在对象创建时设置EvtCleanupCallback事件回调，当驱动程序调用WdfObjectDelete时，框架会自动调用此回调。可以在该回调中调用WdfObjectReference来完成对象删除。
            不管在什么情况下，一旦调用WdfObjectDelete，句柄即告失效
    上下文空间
        每一个WDF框架对象都可以有自己的上下文环境。就像WDM驱动中DEVICE_OBJECT对象的设备扩展一样，如果没有这个设备扩展，大部分WDM驱动都将难以生存。设备扩展作为设备对象的上下文，用来保存和设备相关的资源、信息。除了设备扩展这个供驱动使用的上下文环境之外，其实WDM驱动中还有两个由系统维护的上下文环境，分别是DRIVER_OBJECT对象中的DriverExtension(驱动扩展)和DEVICE_OBJECT对象中的DeviceObjectExtension(系统设备对象扩展)。这二者用来维护系统所需的上下文环境。
        在WDF框架中，上下文环境称为Context Space(上下文空间)。与WDM相比，WDF框架对象的上下文空间具有两个特点
            (1)每个框架对象都可以拥有上下文空间
            (2)每个框架对象可以拥有若干个(数量可以大于1)上下文空间，每个上下文空间由唯一的类型信息结构体(WDF_OBJECT_CONTEXT_TYPE_INFO)来标识。
        WDF框架提供了两种申请上下文空间的方法，可以称为创建时方法和创建后方法，这种区分是针对框架对象的创建来说的。
        WDF的创建时方法实现：
            (1)定义一个结构体，作为上下文空间的内容
            (2)告知结构体长度，即此上下文空间的大小，并同时定义一个将来用以从框架对象中获取上下文空间地址(第一步中定义的结构体变量的指针)的函数。这个函数的类型定义 typedef STRUCT_CONTEXT * FuncGetContextSpace(WDFOBJECT Obj);
            (3)设置对象属性并创建对象
            因为框架对象是不透明的，上下文空间肯定是作为一个变量指针保存在对象中，所以要获得它的任何成员变量，只能采用这种不透明的实现方法。
            一般通过宏WDF_DECLARE_CONTEXT_TYPE_WITH_NAME来定义函数
                WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(STRUCT_CONTEXT,FuncGetContextSpace);
                第一个宏参数是上下文空间结构体的名称，第二个宏参数 FuncGetContextSpace是驱动所起的函数名，驱动只需给出函数名即可，函数的具体定义是由宏实现的。
            还有一个并列的宏，WDF_DECLARE_CONTEXT_TYPE(STRUCT_CONTEXT);宏内部会自动起这样一个函数名:WdfObjectGet_结构体名，对应于结构体STRUCT_CONTEXT，宏为它在内部起的函数名即为WdfObjectGet_STRUCT_CONETXT。该宏定义：#define WDF_DECLARE_CONTEXT_TYPE(_contexttype) WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(_contexttype, WdfObjectGet_ ## _contexttype)
            WDF_DECLARE_CONTEXT_TYPE_WITH_NAME定义：
                #define WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(_contexttype,_castingfunction)
                WDF_DELCARE_TYPE_AND_GLOBALS(
                    _contexttype,WDF_GET_CONTEXT_TYPE_INFO(_contexttype),
                    NULL,WDF_TYPE_DEFAULT_SECTION_NAME)
                WDF_DELCARE_CASTING_FUNCTION(_contexttype,_castingfunction)
            该宏分别执行了另外两个宏:WDF_DELCARE_TYPE_AND_GLOBALS和WDF_DECLARE_CASTING_FUNCTION
            WDF_EXTERN_C表示以C语言方法进行编译。__forceinline，令函数为内联型。
            通过FuncGetContextSpace来获取对象的上下文空间指针。创建时方法完整代码
                typedef struct {...} STRUCT_CONTEXT;
                WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(STRUCT_CONTEXT,FuncGetContextSpace);
                WDFOBJECT gObj;
                void FuncXXX(){
                    WDF_OBJECT_ATTRIBUTES attributes;
                    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attributes,STRUCT_CONTEXT);
                    WdfObjectCreate(&attributes,&Obj);//调用WdfObjectCreate或其他WdfXXXCreate函数创建框架对象
                    STRUCT_CONTEXT * pContext = FuncGetContextSpace(Obj);//通过Obj句柄获取框架对象的上下文空间指针
                    //...
                }
        创建后方法
            (1)初始化一个WDF_OBJECT_ATTRIBUTES结构体，和第一种方法相同
            (2)调用WdfObjectAllocateContext并传入一个对象句柄(已创建者)，为它申请上下文空间。
            实现代码
                typedef struct {...} STRUCT_CONTEXT2;
                WDF_DECLARE_CONTEXT_TYPE_WITH_NAME(STRUCT_CONTEXT2,FuncGetContextSpace2);
                void FuncXXX(){
                    PVOID pContext2;
                    //... gObj被创建
                    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&attributes,DRIVER_CONTEXT2);
                    WdfObjectAllocateContext(gObj,&attributes,&pContext2);
                    ASSERT(pContext2==FuncGetContextSpace2(gObj));
                }
        在大多数情况下仅定义唯一的环境空间，使用一个以上环境空间的情况比较少见。WDF对象框架的这种情况，带来了极大的灵活性。每个对象的环境空间区域都紧跟在对象的后面：
            环境空间地址=对象地址+对象长度
        通过对框架中定义的WdfObjectGetTypedContextWorker函数(WDF框架中实现此接口的函数为:imp_WdfObjectGetTypedContextWorker)进行反汇编，可证明这点。
    PME接口
        WDF框架对象的编程接口类似于PME(Property/Method/Event)接口模型
        对象的属性和方法混在一起，都是以WDF DDI接口的形式暴露的，WDK文档对这二者也没有严格的界定。属性描述对象的特性，每个属性都有对应的Get或Retrieve方法，以及可能存在的Set或Assign方法。比如WdfDeviceGetDeviceState和WdfDeviceSetDeviceState，都是设备对象的属性方法。
        Get/Set系列方法的特点是其操作必定会成功，没有表示正确与否的返回值。而Retrieve/Assign方法则有一个NTSTATUS类型的返回值。
        除了上面的属性接口，所有WDF框架提供的其他接口函数都是方法(Method)接口。如WdfObjectCreate/Delete、WdfDeviceCreate/Delete等，WDF驱动程序通过方法接口对框架对象实施操作。
        事件对WDF驱动至关重要。WDF驱动程序，除了入口函数DriverEntry，其他的都不外事件函数。不是事件函数本身，就是被它调用的子函数。
        本质上，事件函数是回调函数。当创建一个框架对象时，驱动有机会通过属性结构体(WDF_OBJECT_ATTRIBUTES)或其他结构体设置事件回调。当对应的事件发生时，系统就会检查对象是否有对应的事件回调，如果有，就会调用。
        (1)基对象WDFOBJECT事件回调，通过结构体WDF_OBJECT_ATTRIBUTES进行设置。用于WDFOBJECT对象是所有框架对象的组成部分，所以WDFOBJECT对象的事件回调，同时也是所有框架对象的事件回调。调用WdfObjectCreate函数创建WDFOBJECT对象
            NTSTATUS WdfObjectCreate(
                IN OPTIONAL PWDF_OBJECT_ATTRIBUTES Attributes,
                OUT WDFOBJECT* Object);
        其中，参数Attributes是对象属性，WDFOBJECT的事件回调就通过这个参数来设置，可供设置的回调包括：
            PFN_WDF_OBJECT_CONTEXT_CLEANUP EvtCleanupCallback;
            PFN_WDF_OBJECT_CONTEXT_DESTROY EvtDestroyCallback;
        当针对对象句柄的WdfObjectDelete函数被调用时，EvtCleanupCallback将被调用；当对象的引用计数降为0时，EvtDestroyCallback将被调用。一般是，WdfObjectDelete调用导致 EvtCleanupCallback事件，WdfObjectDereference调用把对象的引用计数减为0时，导致 EvtDestroyCallback事件。当两个回调函数存在时，一定是 EvtCleanupCallback回调比 EvtDestroyCallback回调更早被调用。
        (2)子对象事件回调。不同的子对象类型有不同种类的事件回调，由于子对象中包含了一个基对象，所以子对象既可以设置公共的基对象回调，也可以设置子对象回调。框架设备对象的创建函数为 WdfDeviceCreate
            NTSTATUS WdfDeviceCreate(
                IN OUT PWDFDEVICE_INIT* DeviceInit;
                IN OPTIONAL PWDF_OBJECT_ATTRIBUTES DeviceAttributes;
                OUT WDFDEVICE* Device);
        参数 DeviceAttributes用来设置基对象属性。DeviceInit用来设置设备对象的特有属性，可设置的回调较多，包括PNP和电源回调
            VOID WdfDeviceInitSetPnpPowerEventCallbacks(
                IN PWDFDEVICE_INIT DeviceInit,
                IN PWDF_PNPPOWER_EVENT_CALLBACKS PnpPowerEventCallbacks);
        参数 PnpPowerEventCallbacks时一个较大的回调函数数据结构，设置各种PNP和电源事件回调函数。
        并非所有的子对象都有自己的特有事件，比如 WDFREQUEST对象就没有
    DDI接口
        框架的DDI接口即可以从WDK帮助文档中看到的形如WdfXXX的函数
        每个WDF驱动都拥有一个WdfFunctions数组。因为如果所有WDF驱动共用同一个WdfFunctions数组，那么任何一个驱动对它的误操作(例如修改和覆盖)都会导致系统中的其他WDF驱动一起出错。
        数组WdfFunctions的初始化工作是在WdfDriverCreate中完成的。在默认情况下，所有的函数指针都指向WDF框架驱动程序Wdf010000.sys中提供的具体实现。
        很容易利用WdfFunctions这一特点实施内核API Hook操作，针对WDF框架DDI进行安全性测试的工具WDFTester就使用了这种方法。
    父子关系
        WDF的对象模型使用了父子概念，即对象之间存在父子关系。这和C++中的父类、子类是有层次上的区别的：父子对象概念是具体的，类的父子关系则着眼于更高的抽象层次。父对象拥有对子对象的控制权，父对象被销毁前，会先将自己所有的子对象都销毁。父子关系使得对象管理变得方便，对于一个内存对象，不需要总记得是否要释放，只需要维护好它的父对象即可。
        每个驱动都有唯一的驱动对象，驱动对象是所有WDF对象的根对象。在WDF驱动中所有创建的WDF对象，要么是它的子对象，要么是它的某个子对象的子对象，而驱动对象的生命周期是由框架维护的。框架在这方面总能可靠地工作，不用操心去维护任何一个WDF对象，当驱动对象被销毁时，所有子对象都会一起销毁。
        WDF框架对象间的父子关系，是一种典型的树型结构，父对象一定有一个指向子对象列表的指针。

![WDF框架对象间的父子关系](pic/WDF框架对象间的父子关系.png)

        框架对象之间的父子关系，并不能任意搭配。WDFQUEUE对象只能是WDFDEVICE的子对象，而不能是WDFDRIVER的直接子对象。下图实线箭头表示确定的父子关系，长虚箭头表示默认但可改变的父子关系，点虚箭头表示可以多个对象作为父对象

![父子关系图](pic/父子关系图.png)

    对象同步
        框架对象是一种可能被争抢的共享资源。和所有共享资源一样，如果存在争抢，就要为它设置同步机制，框架对象内部默认包含了这种锁机制，在FxObject对象中类型为MxLock的m_SpinLock变量，就是默认的对象锁。
        对于这个默认的对象锁，外部可通过调用WdfObjectAcquireLock和WdfObjectReleaseLock实现手动同步。更加便利的用法是，借助同步机制。同步机制包括
            1.同步范围：有两种可选的同步范围，设备同步(WdfSynchronizationScopeDevice)、队列同步(WdfSynchronizationScopeQueue)。当选择设备同步时，对于设备上的所有队列和文件对象，同一时刻只能有一个对象的一个事件回调被执行；当选择队列同步时，在同一时刻，每个队列只能有一个事件回调被执行。如果不选择任何同步范围，即不同步(WdfSynchronizationScopeNone)，在同一时刻，设备上可以有任意多个事件回调被执行。
                如果是设备同步，则所有下属队列或文件对象的事件回调被执行前，都必须申请设备对象的同步锁；而如果是队列同步，则队列中的事件回调被执行前，都必须申请此队列对象的同步锁。如果不选择任何同步范围，则不必申请同步锁。这是自动同步的实现原理。
                此属性通过结构体 WDF_OBJECT_ATTRIBUTES的 SynchronizationScope变量进行设置。
            2.运行级别：运行级别即事件回调最高可在哪个中断级别(IRQL)上被调用。可选的值只有两个，即运行在PASSIVE_LEVEL(WdfExecutionLevelPassive)，或最高可运行在DISPATCH_LEVEL(WdfExecutionLevelDispatch)。也可以让子设备自动从父设备那里继承此属性，则设置为WdfExecutionLevelInheritFromParent
                此属性通过结构体 WDF_OBJECT_ATTRIBUTES的 ExecutionLevel变量进行设置
                对于设备对象的PNP/Power事件回调，驱动总是对它们实施同步调用的。

### 3.5 驱动对象和设备对象

    驱动对象
        驱动对象是最重要的框架对象，是一切其他框架对象的父对象，也是所有框架对象中第一个被创建，而最后一个被删除的对象。当它的生命周期完结后，所有其他子对象也一定不复存在。
        只要得到驱动对象，就可以顺着它的继承路线，搜索到所有的子对象。由于框架驱动对象处于这个地位，它的作用非常大，能够随时获得这个驱动对象。故而在WDF驱动的任何地方，只要调用WdfGetDriver函数，就可以获得同一个驱动对象句柄
            WDFDRIVER Driver = WdfGetDriver();
        WdfGetDriver调用不需要任何参数，这是因为驱动对象的句柄保全在一个全局结构体变量中，WdfGetDriver直接从结构体变量中获取这个句柄。这个全局结构体类型的定义
            typedef struct _WDF_DRIVER_GLOBALS{
                WDFDRIVER Driver;
                ULONG DriverFlags;
                ULONG DriverTag;
                CHAR DriverName[(32)];
                BOOLEAN DisplaceDriverUnload;
            }WDF_DRIVER_GLOBALS,*PWDF_DRIVER_GLOBALS;
        驱动对象的几个主要作用
            (1)驱动对象代表了加载到系统空间中的驱动模块。相同的驱动文件，不管同时作用于多少个设备，驱动对象总是唯一的。
            (2)在驱动程序的任何地方，调用WdfGetDriver就可以获得唯一的驱动对象句柄。建议把全局变量保存在驱动对象中。
            (3)对于PNP类驱动，驱动对象负责注册EvtDriverDeviceAdd事件回调，这个事件回调相当于WDM架构中的AddDevice函数，用以建立设备栈
            (4)对于非PNP类驱动，一般通过驱动对象注册EvtDriverUnload事件回调，它的作用相当于WDM架构中的DriverUnload函数，保存在驱动对象中的系统资源一般借助EvtDriverUnload事件回调释放。资源泄露在内核中是很严重的错误
            (5)可以为驱动初始化一个事件跟踪(WPP机制)
    驱动入口DriverEntry
        WDF驱动的入口函数(一般为DriverEntry)和框架对象，特别是驱动对象有着非常密切的关系。应当在入口函数中创建驱动对象，在驱动对象被创建之前，一切框架DDI接口都不应该被驱动调用。
        根据驱动类型，DriverEntry入口函数有多种写法，主要分为：设备驱动、过滤驱动和纯软件驱动。所谓的纯软件驱动，不和任何硬件挂钩，是一个在内核中提供接口服务的软件模块
        设备驱动一定要注册EvtDriverDeviceAdd事件回调；过滤驱动根据其类型，如果过滤的设备栈属于某个物理设备，也应当注册EvtDriverDeviceAdd事件回调；否则，驱动加载之后，将不会起到任何预期的作用
        纯软件驱动则不可注册EvtDriverDeviceAdd事件回调；过滤驱动根据其类型，若过滤的设备栈不属于物理设备(如文件驱动设备栈)，则也不可注册此事件回调；否则，将返回无效参数错误
        创建驱动对象，调用WdfDriverCreate接口
            NTSTATUS WdfDriverCreate(
                IN PDRIVER_OBJECT DriverObject,
                IN PCUNICODE_STRING RegistryPath,
                IN OPTIONAL PWDF_OBJECT_ATTRIBUTES DriverAttributes,
                IN PWDF_DRIVER_CONFIG DriverConfig,
                OUT OPTIONAL WDFDRIVER* Driver);
        参数DriverObject类型为内核驱动对象(DRIVER_OBJECT)，这也是唯一WDF驱动中必须用到WDM对象的地方；也进一步说明，框架驱动对象是对内核驱动对象的包装。最后一个输出参数Driver就是包装后的框架设备对象
        参数RegistryPath是驱动所对应服务键在注册表中的路径，这个信息来自内核配置和管理服务器(Cfg Manager)
        参数DriverAttributes是针对WDFOBJECT对象的属性配置的。参数DriverConfig则是专门针对框架驱动对象的属性配置。结构定义如下
            typedef struct _WDF_DRIVER_CONFIG {
                ULONG Size;
                PFN_WDF_DRIVER_DEVICE_ADD EvtDriverDeviceAdd;
                PFN_WDF_DRIVER_UNLOAD EvtDriverUnload;
                ULONG DriverInitFlags;
                ULONG DriverPoolTag;
            }WDF_DRIVER_CONFIG, *PWDF_DRIVER_CONFIG;
        成员Size是结构体的长度，为了方便将来对结构体进行扩展
        成员EvtDriverDeviceAdd和EvtDriverUnload是两个事件回调。前者是当物理设备的设备栈建立时，必须要调用的，是驱动PNP设施的重要部分，其地位相当于WDM驱动中的AddDevice函数；后者是当驱动镜像从内核空间中被卸载时所要调用的，相当于WDM驱动中的DriverUnload函数。
        参数DriverInitFlags用来设置一些初始化标志，可用的有下面两种
            typedef enum _WDF_DRIVER_INIT_FLAGS{
                WdfDriverInitNonPnpDriver = 0x00000001,
                WdfDriverInitNoDispatchOverride = 0x00000002,
            }
        枚举值 WdfDriverInitNonPnpDriver用来区别上述两种不同驱动类型，关系到EvtDriverDeviceAdd事件是否有效
        枚举值 WdfDriverInitNoDispatchOverride用来标志驱动程序是一个小端口驱动，使得WDF框架不仅能够兼容WDM架构，也能兼容小端口架构。一旦设置了小端口驱动标志后，WDF框架将不会用其内部分发函数来处理收到的IRP，而是任由WDF驱动自己继续调用小端口框架的初始化函数来为其设置分发函数。
        第一种驱动类型的入口函数
            NTSTATUS DriverEntry(
                IN PDRIVER_OBJECT DriverObject,
                IN PUNICODE_STRING RegistryPath
            ){
                WDF_DRIVER_CONFIG config;
                NTSTATUS status = STATUS_SUCCESS;
                WDF_DRIVER_CONFIG_INIT(&config,MyEvtDeviceAdd);
                config.EvtDriverUnload =MyEvtDriverUnload;
                return WdfDriverCreate(DriverObject,RegistryPath,WDF_NO_OBJECT_ATTRIBUTES,&config,WDF_NO_HANDLE);
            }
        WDF框架总是把用户创建的WDF驱动默认位PNP类型。非PNP类驱动的入口函数写法
            VOID Unload(IN WDFDRIVER Driver){
                // 如果入口函数中申请了系统资源，可在此处进行释放
                // 用户进程中如果有资源泄露，会随着进程的终结而自动回收全部资源
                // 但内核中没有这种便利，甚至会导致错误检查(BugCheck)和蓝屏
            }
            NTSTATUS DriverEntry(
                IN PDRIVER_OBJECT DriverObject,
                IN PUNICODE_STRING RegistryPath
            ){
                NTSTATUS status;
                WDF_DRIVER_CONFIG config;
                WDFDRIVER driver;
                第二个参数设置为NULL，表示不设置 EvtDriverDeviceAdd事件
                WDF_DRIVER_CONFIG_INIT(&config,NULL);
                //指明这是一个非PNP类驱动
                config.DriverInitFlags = WdfDriverInitNonPnpDriver;
                //一般会设置 EvtDriverUnload事件
                //这使得非PNP类驱动也能够进行"后处理"
                //PNP类驱动的后处理，可在如EvtDeviceD0Exit、EvtDeviceReleaseHardware这类PNP事件中进行
                config.EvtDriverUnload=Unload;
                retrun WdfDriverCreate(DriverObject,RegistryPath,NULL,&config,&driver);
            }
            对于非PNP类驱动，一般会设置其Unload事件回调(EvtDriverUnload)。其原因是，用来进行"后处理"，如释放占用的资源等。PNP类驱动就没有这种必要性，因为PNP类驱动在相关的PNP事件回调(一般是 EvtDeviceD0Exit、EvtDeviceReleaseHardware这两种，代表设备断电和设备移除)中进行后处理最为合适。
    设备对象
        在WDM驱动中，设备对象是驱动程序的核心；但在WDF架构里，设备对象的地位相对低一些，驱动对象的地位则相应上升。设备对象仍然非常重要，隶属于设备对象的事件，占了所有框架事件的四成。与IO相关的操作，依旧是围绕设备对象进行的
        不同的设备对象类型，继承自WDM架构
            功能设备对象(FDO)：功能驱动程序负责为每个设备创建一个FDO，在设备栈中它位于物理设备对象(PDO)的上层
            物理设备对象(PDO)：一个由总线驱动创建的PDO，在逻辑上代表了物理设备本身，而功能设备对象(FDO)则代表了系统针对这个PDO所做的处理。FDO之所以由某个总线驱动创建，是因为此FDO所代表的物理设备连接到了此总线设备上(此时，此总线驱动承担了总线设备的功能驱动作用)。
            过滤设备对象(Filter DO)：过滤设备对象是设备栈的不速之客，可以位于设备栈的任何一个位置，即它可以对任何一个设备栈中既存的设备对象进行过滤。最精简的设备栈，往往只有两个设备对象，即FDO和PDO，正是由于若干个Filter DO的加入，设备栈才热闹起来
            控制设备对象(CDO)：一般不存在于设备栈中，而是一个独立的设备(如果有Filter DO愿意过滤它，也就构成了设备栈)。这个设备用来作为用户程序的接口，用户程序通过CreateFile将之打开，并通过它发送一些IO请求给驱动程序处理。这正式其名字由来，用户程序通过它内核驱动实现控制
        设备对象有很多设备相关的属性，这一点和驱动对象不同，驱动对象暴露出的属性，只有驱动在注册表中的服务键路径这一个(WdfDriverGetRegisterPath)。用一个列表来描述设备对象的所有属性，暴露出的属性可通过WdfDeviceSetXXX、WdfDeviceInitXXX系列函数来设置，或通过WdfDeviceGetXXX系列函数来获取。下表是最常用的一些设备对象属性及简单描述，并附上了设置和获取接口
            属性名  描述    DDI
            对齐    设备地址对齐，便于内存操作。源自DEVICE_OBJECT结构体中的AlignmentRequirement变量 WdfDeviceSetAlignmentRequiremenet/WdfDeviceGetAlignmentRequiremenet
            名称    唯一的设备名称  WdfDeviceInitAssignName/无获取接口
            安全ID  针对设备对象的安全属性  WdfDeviceInitAssignSDDI.String/无获取接口
            默认IO队列  如果为IO请求创建指定的IO队列，则所有IO请求都进入到默认队列中    不能设置/WdfDeviceGetDefaultQueue
            设备特征    掩码形式的设备特征值，源自DEVICE_OBJECT结构体中的Characteristics变量    WdfDeviceInitSetCharacteristics & WdfDeviceSetCharacteristics/WdfDeviceGetCharacteristics
            PNP特征 包括是否支持软件删除(Eject)、异常拔除、能够Dock设备(如Hub)等特性，见WDF_DEVICE_PNP_CAPABILITIES WdfDeviceSetPnpCapabilities/无获取接口
            电源特征    包括电源映射(Dx到Sx)、唤醒等特性，见WDF_DEVICE_POWER_CAPABILITIES   WdfDeviceSetPowerCapabilities/无获取接口
            状态    设备状态，可用的设备状态包括可用、禁止、移除等  WdfDeviceSetDeviceState/WdfDeviceGetDeviceState
            PNP状态 设备PNP状态，只有PNP设备才有。非常复杂，见枚举类型WDF_DEVICE_PNP_STATE  不能设置/WdfDeviceGetDevicePnpState
            电源状态    设备电源状态，见枚举类型WDF_DEVICE_POWER_STATE  不能设置/WdfDeviceGetDevicePowerState
            电源策略状态    包括闲时休眠等，见枚举类型WDF_DEVICE_PWOER_POLICY_STATE 不能设置/WdfDeviceGetDevicePowerPolicyState
            电源策略所有者  总是让设备的功能驱动作为设备的电源策略所有者。设备栈中只能有一个这样的设备对象，否则会发生冲突  WdfDeviceInitSetPowerPolicyOwnership/无获取接口
            过滤设备对象(Filter DO) 根据是否是过滤设备对象，框架对IO请求的处理有一些差异    WdfFdoInitSetFilter/无获取接口
            默认IO目标对象  框架将设置栈中的下一层设备对象封装成默认IO目标对象  不能设置/WdfDeviceGetIoTarget
    创建设备对象
        内核服务或非PNP类驱动都会创建CDO对象，以接收来自用户程序的控制信息。PNP类驱动应当在EvtDriverDeviceAdd事件中创建设备对象，是最理想的场所。但内核服务或非PNP类驱动不可能接收到EvtDriverDeviceAdd事件，所以应该在入口函数中创建CDO对象
            //和在WDM中一样，把设备对象作为全局对象保存
            WDFDEVICE wdfDevice;
            //驱动入口函数
            NTSTATUS DriverEntry(
                IN PDRIVER_OBJECT DriverObject,
                IN PUNICODE_STRING RegistryPath
            ){
                WDFDRIVER driver;
                PWDFDEVICE_INIT deviceInit;
                PDEVICE_OBJECT deviceObject;
                NTSTATUS status;
                //创建框架驱动对象，具体实现省略
                WdfDriverCreate(...,&driver);
                //Allocate a device initialization structure
                deviceInit=WdfControlDeviceInitAllocate(driver,&SDDL_DEVOBJ_KERNEL_ONLY);
                //Set the device characteristics
                WdfDeviceInitSetCharacteristics(deviceInit,FILE_DEVICE_SECURE_OPEN,FALSE);
                //Create a framework device object
                status=WdfDeviceCreate(deviceInit,WDF_NO_OBJECT_ATTRIBUTES,&wdfDevice);
                //Check status
                if(status == STATUS_SUCCESS){
                    //Initialization of the frame device obejct is complete
                    WdfControlFinishInitializing(wdfDevice);
                    //Get the associated WDM device object
                    deviceObject=WdfDeviceWdmGetDeviceObject(wdfDevice);
                }
                return status;
            }
        有了这一个设备对象后，就等于建立了和用户程序之间的通信桥梁
    设备栈
        设备栈并没有因为WDF框架的加入而有所变化，但IRP包在设备栈中的流动却会有所改变。
        设备栈举例分析：这个设备栈由三个设备对象组成，最上层的是功能设备对象，中间的是过滤设备对象，最底层的是物理设备对象。是很普通的一个设备栈，假设这个设备栈处于两个完全不同的驱动栈中，一个是3个设备所属的驱动：全部是WDM驱动；另外两个相反，都是WDF驱动。当一个IRP在这两个本质一样的设备栈中流过的时候，区别：

![IRP的流动](pic/IRP的流动.png)

        左图是正常的情况，而右图中，IRP依旧在设备栈中传递，但当进入WDF驱动中后，到了设备对象(DEVICE_OBJECT)中的IRP，会被封装为WDF IO请求对象(即WDFREQUEST)，送给WDF设备(WDFDEVICE)去处理；处理完后，WDF设备对象再从WDFREQUEST对象中提取出IRP，并把IRP传递到设备栈中的下一层。
        如果要控制WDF驱动中的IRP刘翔，比如不让IRP流到WDF设备对象中，可以通过函数 WdfDeviceInitAssignWdfIrpPreprocessCallback 注册一个名为EvtDeviceWdfIrpPrece的事件函数，在事件函数中按照WDM的方式处理IRP，包括传递到下层设备，或者完成IRP操作

### 3.6 IO模型

    系统的IO请求机制并没有改变，即IO管理器对IO请求仍然是封装成IRP结构体发往内核驱动的，并不管它是WDM模式还是WDF模式。但WDF框架收到IRP后，有足够的睿智判断出此请求是直接在框架内部处理，还是调用WDF驱动注册过的事件回调，交回驱动处理。如果调用事件回调，就必须将IRP封装成框架请求即WDFREQUEST对象
    如此，所有IRP都进入到框架中来，一般情况下，WDF是不可能直接对IRP进行操作的。WDF驱动不用为IRP担负任何责任。
    另一方面，所有的WDFREQUEST对象都是从框架中创建并流向WDF驱动的。可以把框架和驱动理解成一对一的关系，框架对一切都有很好的规划，尽量让驱动减轻负担。就拿WDFREQUEST对象来说，框架对所有流出它的对象都了如指掌，并自动维护它们的生命周期，不用WDF驱动操心
    IO目标对象

![目标对象的内部逻辑](pic/目标对象的内部逻辑.png)

        上图可以看到，WDFDEVICE对象对WDM设备对象(DEVICE_OBJECT)进行了封装。WDFDEVICE对象仅仅保存了一个指向 DEVICE_OBJECT的指针。还有另外一类对象，称为WDFIOTARGET(IO目标对象)。WDFIOTARGET对象也对 DEVICE_OBJECT进行了封装，但它和 WDFDEVICE对象的不同之处在于：只有唯一的 WDFDEVICE对象与WDM设备对象关联，因为框架不会允许多个 WDFDEVICE对象对应于同一个WDM设备对象——因为无法从 DEVICE_OBJECT对象反推出 WDFDEVICE对象(DEVICE_OBJECT对象不知道外面有一个 WDFDEVICE对象)，如果不采用一一对应的策略，在管理上一定会混乱。
        WDFDEVICE和 DEVICE_OBJECT对象的一一对应也有不足之处，无法实现：在另一个WDF驱动(Driver2)中发送命令给当前驱动(Driver1)的设备对象(WdfDevice)
        首先Driver1是设备对象WdfDev(它封装了 DEVICE_OBJECT对象Dev)的拥有者，框架不允许Driver2也拥有一个等效的设备对象(不存在另一个封装了Dev对象的WdfDev2对象)。所以Driver2要想通过设备对象句柄发送请求，是无法实现的。框架有一个严格规定，框架对象不能在驱动之间传递
        解决方法是，引入WDFIOTARGET对象。上图代表 WDFIOTARGET对象的有三个，一个是本地的 WDFIOTARGET对象，也称为默认 WDFIOTARGET对象，本地的 WDFIOTARGET对象是唯一的，框架创建 WDFDEVICE对象时也顺便创建了它，并令二者一一关联。以及若干远程 WDFIOTARGET对象，远程对象可以一个都没有，也可以创建更多。当别的驱动程序或本驱动程序的其他地方(如果驱动中存在多个设备栈)要发送命令到此设备对象时，可以通过远程 WDFIOTARGET对象来完成。
        不论是本地的还是远程的 WDFIOTARGET对象对象，总有一个队列与此相关联。若一个驱动程序通过本地 WDFIOTARGET对象发送IO请求到此设备对象，则此IO请求要到QUEUE3中排队；若另一驱动程序通过远程 WDFIOTARGET对象1发送IO请求，则此请求要到QUEUE1中排队。在这种机制下，设备对象退居其次，由IO目标对象作为上层设施，对来自各个方向的请求进行条分缕析的分类与管理
        队列带来了一些好处，由于设备对象的缺陷，所以在IO请求的处理上，WDF框架只知目标对象，不知设备对象，把IO请求发送到目标对象中。各个目标对象是单独运行的，能够实现一些高阶的功能，比如把远程目标对象1删除，此目标对象队列上的所有IO请求都被删除，而其他目标对象上的IO请求并不受影响。
        经典名言：“只要多添加一个简介层，计算机科学中就没有对此解决不了的问题”。IO目标对象就是设备对象的一个简介层，给旧的IO请求处理带来一些新特性
    IO目标对象的细节
        IO目标是对IO请求将发送到的目标驱动的描述。例如，向另一个内核驱动中的设备发送一个IOCTL命令，这个远程设备对象就是IOCTL命令的IO目标(IO Target)
        新定义的对象，赋予了很多实用的妙处
            (1)请求以同步方式发送到IO目标对象
            (2)请求以异步方式发送到IO目标对象
            (3)为发送到IO目标的请求设置超时，如果预期时间内仍未完成，就取消请求
            (4)IO目标对象可以被启动、停止、关闭，只有启动后的IO目标对象才能接收请求，否则将关闭外界请求通道
            (5)跟踪并维护发送到IO目标的IO请求。比如删除目标对象后，所有排队于其中的IO请求对象都将被删除。
        WDFIOTARGET对象是设备的封装，调用 WdfIoTargetGetDevice函数可以获取被封装的设备对象句柄
            WDFDEVICE WdfIoTargetGetDevice( IN WDFIOTARGET IoTarget);
        IO目标对象分为普通对象和特殊对象两种，普通目标对象就是 WDFIOTARGET，特殊目标对象目前只有一种，即USB IO目标对象。USB IO目标对象并没有一个对应的类型被暴露出来，而是隐藏在诸如 WDFUSBDEVICE、WDFUSBPIPE这些对象内部，然后通过这些对象句柄来使用特殊IO目标对象。借助特殊目标对象可以轻易地实现许多USB功能，大大简化了代码设计
        普通IO目标对象，即 WDFIOTARGET对象分为本地和远程两种，在有些资料中，本地IO目标对象还被称为默认(default)对象。如果某个请求继续在当前设备栈中传递，则对应的 WDFIOTARGET对象为本地的；若被传递到其他的设备栈中，不管此设备栈是否也通过本驱动，则对应的 WDFIOTARGET对象通称为远程的
        可以直接从设备对象中获取 WDFIOTARGET对象，所获取的对象对应着当前设备栈中的下一层设备
            WDFIOTARGET WdfDeviceGetIoTarget( IN WDFDEVICE Device);
        通过此方式获取的 WDFIOTARGET对象，称为此设备对象的本地(或默认) WDFIOTARGET对象，凡是发送到此设备对象的 WDFREQUEST对象若要在设备栈中继续传递，则应当将请求发送到此本地目标对象。一个默认事件回调函数可实现如下
            void SomeEvtCallback( WDFDEVICE Device, WDFREQUEST Request){
                WdfRequestSend(Request, WdfDeviceGetIoTarget(Device) ,NULL);
            }
        使用一个远程IO目标对象需要经过两个步骤：第一步，创建远程IO目标对象；第二步，打开(Open)此对象。调用WdfIoTargetCreate接口新建一个IO目标对象：
            NTSTATUS WdfIoTargetCreate(
                IN WDFDEVICE Device,
                IN OPTIONAL PWDF_OBJECT_ATTRIBUTES IoTargetAttributes,
                OUT WDFIOTARGET * IoTarget
            );
        参数Device是被创建的IO目标对象的拥有者，在默认情况下，就是被创建的IO目标对象的父对象(可通过在IoTargetAttributes中设置 ParentObject改变此默认情况)。参数IoTarget Attributes用来设置新建 WDFIOTARGET对象的属性，可直接传入 WDF_NO_OBJECT_ATTRIBUTES。参数IoTarget返回新建的目标对象，一个新建的目标对象是“空的”，并没有和任何“目标”相关联。所以在正式被使用前，还需要通过调用 WdfIoTargetOpen接口函数将它打开，并和一个“目标”挂钩。
        WDFIOTARGET对象有一个状态标志，它可以处于启动、停止和终止等状态。只有当一个 WDFIOTARGET对象处于启动状态时，发送到它的IO请求才会被处理；否则将根据策略，可能被抛弃，也可能被放入队列中等待启动后再处理
            NTSTATUS WdfIoTargetStart( IN WDFIOTARGET IoTarget);
        此接口函数用来启动一个 WDFIOTARGET对象；相应地，还存在停止与终止接口：
            NTSTATUS WdfIoTargetStop( IN WDFIOTARGET IoTarget);
            NTSTATUS WdfIotargetClose( IN WDFIOTARGET IoTarget);
        由于只有 WDFIOTARGET对象启动之后，IO请求才能被正确处理，所以在传递请求前先查看 WDFIOTARGET对象的状态。调用 WdfIoTargetGetState驱动当前状态：
            WDF_IO_TARGET_STATE WdfIoTargetGetState(WDFIOTARGET Tar);
        枚举类型WDF_IO_TARGET_STATE定义了所有的 WDFIOTARGET对象状态：
            typedef enum _WDF_IO_TARGET_STATE{
                WdfIoTargetStateUndefined = 0,
                WdfIoTargetStarted,
                WdfIoTargetStopped,
                WdfIoTargetClosedForQueryRemove,
                WdfIoTargetClosed,
                WdfIoTargetDeleted,
            } WDF_IO_TARGET_STATE, *PWDF_IO_TARGET_STATE;
        状态 WdfIoTargetStateUndefined是无效状态，框架内部会使用，驱动程序不会收到这个状态值，也不可以使用
        状态 WdfIoTargetStarted表示目标对象已经启动，本地目标对象默认总是处于启动状态，除非驱动程序自己让它处于停止状态。
        状态 WdfIoTargetStopped表示目标对象被停止，此时目标对象根据停止操作中的Action参数来处理接收到的IO请求
        状态 WdfIoTargetClosedForQueryRemove表示目标对象所代表的设备对象请求移除，故而不久设备将被移除
        状态 WdfIoTargetClosed表示目标设备所代表的设备对象已经被移除，不仅驱动再也不可以发送任何IO请求到此目标对象，而且目标对象原有的Pending请求也已经被取消(Cancel)，被关闭的IO目标对象可通过 WdfIoTargetOpen再次开启(Open)
        状态 WdfIoTargetDeleted表示目标设备所代表的设备对象已经被删除(Delete)，目标设备与设备对象都不再可用
    安全的缓冲区
        缓冲区安全是老生常谈的问题。引入缓冲区溢出的根本原因是对缓冲区的长度缺乏必要的警醒，一个简单的解决方法是，把缓冲区长度作为缓冲区的一部分，和缓冲区指针放在一起。以后凡是使用缓冲区指针的地方，都必须判断其长度(以及有效长度，如果缓冲区已经被部分用过)，并据此进行安全操作。
        有两个很好的例子实现了这条策略。在用户环境下，VS编译器实现的新的安全CRT字符串处理函数如strcat_s、sprintf_s等，代替了原先不安全的字符串函数(即strcat和sprintf)，其实现方法是新增字符串长度作为函数输入参数；内核驱动中广泛使用的UNICODE_STRING结构体，把缓冲区长度和有效长度作为结构体的一部分，从而让所有的RtlUnicodeStringXXX函数都置于安全环境之下
        在WDF框架中，所有的IO请求对象都使用了WDFMEMORY对象来表示输入/输出缓冲区。WDFMEMORY对象的定义同样实践了上述缓冲区安全规则。WDFMEMORY对象的几个特点
            (1)内部维护了三个数据：内存区指针、内存区长度、有效长度(字符串长度)。这使得内存对象是安全的。
            (2)维护内存区生命周期：如果内存区是由框架申请的，则框架将最终负责内存区释放；如果是由WDF驱动创建的，则由驱动自己负责释放
            (3)可以使用内存区的任意部分，这通过指定一个偏移值(offset)来实现。在这种情况下，实际可用的内存区长度总是总长度减去偏移值。
        创建 WDFMEMORY 对象的方法有两种。第一种方法是由框架申请内存空间。在这种方法下，根据从哪里申请内存，又能分出两种子方法，第一种子方法是由内存池中申请
            NTSTATUS WdfMemoryCreate(
                IN OPTIONAL PWDF_OBJECT_ATTRIBUTES Attributes,
                IN POOL_TYPE PoolType,
                IN OPTIONAL ULONG PoolTag,
                IN size_t BufferSize,
                OUT WDFMEMORY* Memory,
                OUT OPTIONAL PVOID* Buffer
            );
        参数 PoolType、PoolTag和BufferSize用来在内部申请内存时，作为必要的参数传入；而可选参数Buffer则返回这个内存区指针，函数内部会有调用：
            Buffer = ExAllocatePoolWithTag(poolType, BufferSize, PoolTag)
        所以相关参数都应该遵循内存申请的基本原则，比如，如果要在高中断级上使用，则应该让PoolType值为NonPagedPool；参数Memory时新创建的对象句柄。使用这种方法创建的内存对象，内存缓冲区将在WdfObjectDelete被执行时和对象一起销毁
        第二种子方法是从旁视列表中申请内存
            NTSTATUS WdfMemoryCreateFromLookaside(
                IN WDFLOOKASIDE lookaside,
                OUT WDFMEMORY* Memory
            );
        参数Lookaside是一个框架旁视列表对象句柄，是通过 WdfLookasideListCreate方式创建的。旁视列表是一块预先分配好的内存区域，如果旁视列表中的内存用光，则依旧去内存池中申请。使用旁视列表的好处就是快速
        创建内存对象的第二种方法是预先申请好内存后，再交给框架封装
            NTSTATUS WdfMemoryCreatePreallocated(
                IN OPTIONAL PWDF_OBJECT_ATTRIBUTES Attributes,
                IN PVOID Buffer,
                IN size_t BufferSize,
                OUT WDFMEMORY* Memory
            );
        参数Buffer指向预先申请好的一块内存，申请的方式不重要(内存池或旁视列表)；参数 BufferSize是这块内存区的字节长度
        使用第二种方法创建的内存对象，对它所控制的内存区并无维护义务，这与第一种方法不同。驱动调用WdfObjectDelete将此内存对象删除，将仅删除对象本身，内存区并不释放而依旧有效。这种方法的另一个好处是可以随时替换对象的内存缓冲区
            NTSTATUS WdfMemoryAssignBuffer(
                IN WDFMEMORY Memory,
                IN PVOID Buffer,
                IN size_t BufferSize
            );
        参数Buffer和BufferSize代表了新的内存缓冲区。调用此函数后，原来的内存区将被替换掉(但并没有被释放，依旧有效、可用)
        内存对象于内存缓冲区是一一对应的，可以通过 WdfMemoryGetBuffer获取内存对象的内存区指针
            PVOID WdfMemoryGetBuffer(
                IN WDFMEMORY Memory,
                OUT OPTIONAL size_t* BufferSize
            );
        可选参数BufferSize返回缓冲区长度，缓冲区指针通过返回值返回给调用者。
        内存对象的函数较为简单，对应写入和读出
            NTSTATUS WdfMemoryCopyFromBuffer(
                IN WDFMEMORY DestinationMemory,
                IN size_t DestinationOffset,
                IN PVOID Buffer,
                IN size_t NumBytesToCopyFrom
            );
            NTSTATUS WdfMemoryCopyToBuffer(
                IN WDFMEMORY SourceMemory,
                IN size_t SourceOffset,
                IN PVOID Buffer,
                IN size_t NumBytesToCopyTo
            );
        第一个函数用来将指定内存区的内容写入内存对象中。参数 DestinationMemory和 DestinationOffset代表了内存对象和内部偏移；参数Buffer代表了外部缓冲区；参数 NumBytesToCopyFrom表示应将外部缓冲区的多少内容写入内存对象中。
        第二个函数用来将内存对象中的内容写入指定外部内存区中。参数 SourceMemory和 SourceOffset代表了内存对象和内部偏移；参数 Buffer代表了外部缓冲区；参数 NumBytesToCopyTo则表示准备将多少内容拷贝到外部缓冲区，此值不应该大于外部缓冲区的实际长度，否则就要溢出了。
        这两个函数内部都有安全检测，对于第一个函数，如果 NumBytesToCopyFrom比内存对象的有效空间(内存区长度减去偏移值 DestinationOffset大)，则函数将返回错误值 STATUS_BUFFER_TOO_SMALL；或者若指定的偏移值 DestinationOffset超过了内存区范围，函数也能检测到此uowu，并返回 STATUS_INVALID_BUFFER_SIZE
    内存对象(一)
        WDFREQUEST对象的所有缓冲区，都是由 WDFMEMORY对象封装的。这带来的一个好处就是，内核驱动不用为用户缓冲区类型担心了。IRP中的用户缓冲区有3种类型，即 METHOD_BUFFERED、METHOD_DIRECT、METHOD_NEITHER。这3种类型的缓冲区指针分别存储在IRP结构体的不同地方。
        对于 METHOD_BUFFERED、METHOD_DIRECT这两种缓冲类型的IO请求，使用下面的方法获取对应的内存指针
            NTSTATUS WdfRequestRetrieveInputMemory(
                IN WDFREQUEST Request,
                OUT WDFMEMORY* Memory
            );
            NTSTATUS WdfRequestRetrieveOutputMemory(
                IN WDFREQUEST Request,
                OUT WDFMEMORY* Memory
            );
        这两个函数，传入一个 WDFREQUEST句柄，就能返回一个 WDFMEMORY对象句柄。这两个函数的返回值传达了一些重要信息
            如果返回值为 STATUS_INTERNAL_ERROR，表明传入的 WDFREQUEST对象已经处理完成，在此情况下，不可以再去获取其内存或缓冲区
            如果返回值为 STATUS_BUFFER_TOO_SMALL，表明缓冲区长度为0，即缓冲区不存在
            如果返回值为 STATUS_INVALID_DEVICE_REQUEST，代表错误的请求对象类型，即传入的 WDFREQUEST对象的类型错了。
        不是所有类型的 WDFREQUEST对象都可以使用上述两个函数，必须要满足下面3个条件
            (1)对于Input函数，只有写、设备IO控制两种命令才可以调用；对于OUTPUT函数，只有读、设备IO控制两种命令才可以调用。此处设备IO控制命令，是指请求码为 IRP_MJ_DEVICE_CONTROL和 IRP_MJ_DEVICE_INTERNAL_DEVICE_CONTROL的两种IO请求
            (2)必须保证IO命令的缓冲方式是 METHOD_BUFFERED、METHOD_DIRECT这两种
            (3)如果IO缓冲方式是 METHOD_NEITHER，有两种情况也是正确的：IO请求来自内核模块，而非用户程序；IO请求码为 IRP_MJ_INTERNAL_DEVICE_CONTROL。这两种情况都能保证这一点：缓冲指针指向系统空间，而非用户空间
        如果不能满足上述3个条件，会得到 STATUS_INVALID_DEVICE_REQUEST错误
        可以通过 WDFMEMORY对象句柄获取其缓冲区指针
            NTSTATUS WdfRequestRetrieveInputBuffer(
                IN WDFREQUEST Request,
                IN size_t MinimumRequiredSize,
                OUT PVOID* Buffer,
                OUT size_t* Length
            );
            NTSTATUS WdfRequestRetrieveOutputBuffer(
                IN WDFREQUEST Request,
                IN size_t MinimumRequiredSize,
                OUT PVOID* Buffer,
                OUT size_t* Length 
            );
        输出参数Buffer和Length分别用来返回缓冲区指针及其长度。这两个函数的一个好处是它们各有一个 MinimumRequiredSize参数。驱动在获得缓冲区后，必定要先验证一下其有效性，最简单的验证方法就是通过缓冲区长度进行验证。比如某设备IO控制请i去，需要请求者传入一个结构体参数，若输入缓冲区长度小于结构体长度，则说明这个输入参数有错误；如果缓冲区长度小于 MinimumRequiredSize(或等于0)，则返回错误 STATUS_BUFFER_TOO_SMALL。若驱动程序不想做长度判断，只要将此值设为0即可，因为长度是一个正整数，一定大于等于0
        另外，不仅可以直接返回缓冲区指针，而且可以返回MDL指针，这个MDL对缓冲区进行封装，使用下面两个函数
            NTSTATUS WdfRequestRetrieveInputWdmMdl(
                IN WDFREQUEST Request,
                OUT PMDL* Mdl
            );
            NTSTATUS WdfRequestRetrieveOutputWdmMdl(
                IN WDFREQUEST Request,
                OUT PMDL* Mdl
            );
        这两个函数和前面函数相比，除了缓冲区的返回方式不同外，其他的都是一样的。驱动对象不必为得到的MDL指针调用IoFreeMdl，应由框架自己维护
    内存对象(二)
        如果使用 METHOD_NEITHER缓冲方式的IO请求不是来自用户程序，而是来自内存模块，则获取缓冲区的方式和前两种一样。如果IO请求来自用户程序，则缓冲区是在用户空间中申请的，在内核中使用用户缓冲，有很多限制，要与指定的进程上下文相关才有效。所以，获取缓冲区的方式变得复杂，必须首先把用户地址转变为能够在内核中自用使用的内核地址。
        在WDF框架中，所有交由WDF驱动处理的IO请求，都是先入队等候，再交付设备对象处理的。由于这样一个入队等候过程，将导致IO请求以异步方式被处理。而一个用户指针在内核中若以异步方式使用，会出现问题，因为内核所对应的用户进程环境是在不断变化的。唯一的办法就是，在IO请求入队前——此时仍处于请求发送者进程环境——将用户地址所代表的内存页锁定到内存，并重新映射到一个内核地址。

![METHOD_NEITHER内存处理方法](pic/METHOD_NEITHER内存处理方法.png)

        当用户进程将一个请求发送到内核中时，由于框架代理了内核驱动的所有接口，所以WDF框架能够首先得到这个IO请求，并将它封装成IO请求对象。此时内核恰恰处于发送请求进程的上下文环境，用户指针是有效的。
        第一步，是抢在IO请求对象入队前，将其用户指针转换为内核指针。两个小黑球代表了IO请求对象的两个状态，虚线方框代表了两个不同的虚拟地址区域(其物理地址都是同一块)
        第二步，是正常入队
        第三步，代表了等待过程，入队后何时被处理是不确定的，即异步
        第四步，发送给WDF驱动处理，必须使用内核指针
        WDF驱动可以通过DDI接口 WdfDeviceInitSetIoInCallerContextCallback 注册一个 EvtIoCallerContext 回调函数，在一个WDFREQUEST对象被放入队列之前对它进行“前处理”。这是唯一可以进行“前处理”的回到，所有其他的事件回调的时机都是在IO请求入队之后。此回调函数原型：
            VOID EvtIoCallerContext(
                IN WDFDEVICE Device,
                IN WDFREQUEST Request
            );
        应当根据参数 Request判断其请求类型并获取其缓冲方式，若是 METHOD_NEITHER就进行下述相关处理
        (1)获取缓冲区指针，用 WdfRequestRetrieveUnsafeUserInputBuffer和 WdfRequestRetrieveUnsafeUserOutputBuffer两个函数
            NTSTATUS WdfRequestRetrieveUnsafeUserInputBuffer(
                IN WDFREQUEST Request,
                IN size_t MinimumRequiredLength,
                OUT PVOID* InputBuffer,
                OUT OPTIONAL size_t* Length
            );
            NTSTATUS WdfRequestRetrieveUnsafeUserOutputBuffer(
                IN WDFREQUEST Request,
                IN size_t MinimumRequiredLength,
                OUT PVOID* OutputBuffer,
                OUT OPTIONAL size_t* Length
            );
        这两个函数一定要在 EvtIoCallerContext事件回调中调用，否则就会返回错误
        若IO请求的缓冲类型不是 METHOD_NEITHER，则调用这两个函数都会返回错误。一个IO请求，如果能够用第一种方法正确获取缓冲，则必不能用此处的两个函数获取其缓冲；反之亦然
        (2)正确获取用户缓冲区指针后，要将此指针所代表的虚拟地址所指向的内存页锁定在物理内存中(所谓锁定，就是确保不被换出到外部页文件中，而一直保持在物理内存中)。对于读请求，调用函数 WdfRequestProbeAndLockUserBufferForRead 以锁定内存页：写请求则调用函数 WdfRequestProbeAndLockUserBufferForWrite 以锁定内存页。这两个函数正如其名所示，会先验证所传入的地址是否有效(Probe)，然后锁定(Lock)它。
            NTSTATUS WdfRequestProbeAndLockUserBufferForRead(
                IN WDFREQUEST Request,
                IN PVOID Buffer,
                IN size_t Length,
                OUT WDFMEMORY* MemoryObject
            );
            NTSTATUS WdfRequestProbeAndLockUserBufferForWrite(
                IN WDFREQUEST Request,
                IN PVOID Buffer,
                IN size_t Length,
                OUT WDFMEMORY* MemoryObject
            );
        上述两个函数除了会验证Buffer地址的有效性外，还会做一项有意义的验证，即判断当前线程是否是Request对象的创建者线程。如果不是，就会返回错误。这一点非常实用，它确保只在正确的进程上下文中处理用户缓冲。
        (3)为IO请求申请一个上下文空间(Context Space)，并将得到的内存对象句柄保存到上下文空间中。可以通过内存 WdfObjectAllocateContext函数为指定框架对象申请上下文空间，那么以后正式处理此IO请求时(在队列中处理)，可以通过上下文空间获取内存对象，并通过内存对象获取输入/输出缓冲区。不可在正式处理时，通过第1步中的方法获取缓冲区
        (4)此时，Request对象的缓冲区已经转换到内核空间了。应令此Request对象顺利入队(进入指定的框架队列)，并随后通过队列再次将此Request经由事件回调传回WDF驱动处理。通过 WdfDeviceEnqueueRequest方法让一个IO请求入队
            NTSTATUS WdfDeviceEnqueueRequest(
                IN WDFDEVICE Device,
                IN WDFREQUEST Request
            );
        此函数也只能EvtIoCallerContext事件回调中调用，否则会返回错误。
        上述过程很复杂，以下是 EvtIoCallerContext的实现例子。此例子中，首先获取请求类型，仅对 WdfRequestTypeDeviceControl请求做处理(即 IRP_MJ_DEVICE_CONTROL)。获取与此命令相关的IOCTL控制码，并根据末两位判断缓冲区类型，若是 METHOD_NEITHER，则按照上述4个步骤来处理
    框架和IO请求

![框架和IO请求](pic/框架和IO请求.png)

        第1步，应用程序调用Kernel32中的接口函数ReadFile进行读操作
        第2步，ReadFile函数调用Ntdll.dll中的原生函数NtReadFile，从而陷入内核并调用内核服务NtReadFile，IO管理器将接管读操作处理
        第3步，IO管理器为读请求构造类型为 IRP_MJ_READ的IRP
        第4步，IO管理器找到由WDF框架创建的设备对象(DEVICE_OBJECT)，并将IRP发送到它的读分发函数(DispatchRead)
        第5步，WDF框架收到IRP后，查看WDF驱动是否注册了读回调，如果注册了就将IRP封装成一个IO请求对象(WDFREQUEST)，并把它放到了WDF驱动的某个指定队列中
        第6步，队列将IO请求对象发送给WDF驱动处理，WDF驱动注册的读回调被执行
    更详细的处理流程
        框架收到IO管理器传递给它的IRP请求后，将IRP封装在 WDFREQUEST对象中，并作为参数调用驱动注册的事件回调函数。
        首先看 WDFREQUEST对象的创建过程
        IO管理器将用户请求封装成IRP对象并发送到指定的设备栈。首先得到IRP的是WDF框架，框架对IRP做一定处理后，检查WDF驱动是否注册了所需要的事件回调，如果没有注册，框架就自己将IRP发送到设备栈的下层设备，IRP将得到处理，并最终返回到IO管理器
        在WDF驱动注册了事件回调的情况下，只有在下述情况下框架才会创建 WDFREQUEST对象：IRP对象类型为 IRP_MJ_CREATE、IRP_MJ_DEVICE_CONTROL、IRP_MJ_READ、IRP_MJ_WRITE、IRP_MJ_INTERNAL_DEVICE_CONTROL五者之一
        创建的 WDFREQUEST对象通过参数传递到事件回调中，WDF驱动通过 WdfRequestXXX系列函数处理对象，比如，发送到底层设备栈，直接完成请求。也可以调用DDI接口函数 WdfRequestWdfGetIrp，从对象中获取IRP结构体并以WDM方式处理
        如果框架检查发现IRP的命令类型并非上述五种之一，则不会创建 WDFREQUEST对象，这样WDF驱动即使注册了事件回调，也不能拥有对命令进行最终处理的机会，框架把最终的处理权留给了自己。比如，与 IRP_MJ_CLEANUP命令相应的事件回调函数定义如下：
            VOID EvtCleanupCallback( IN WDFOBJECT Object)
        CleanUp回调函数能够针对设备对象做一些有限的处理，但对于CleanUp命令无任何权力。由于此回调函数返回值为void，也不能通过其返回值来影响框架的下一步处理
        所有的PnP/电源事件回调都不接受 WDFREQUEST参数，所以WDF驱动都没有权利直接干预PnP/电源命令的最终处理，而只能根据PnP电源/状态迁移对设备进行相应的处理。这种方法避免了WDF驱动可能会做出的一些错误。
        如果命令继续在设备栈中传递(即第二种情况)，则WDF驱动有机会完成"后处理"操作，通过注册完成函数来实现对IO请求的"后处理"。用户既可以通过IRP调用 IoSetIrpCompletionRoutine注册完成函数，也可以通过 WDFREQUEST对象调用接口函数 WdfRequestSetCompletionRoutine注册完成回调。

![框架处理客户请求的过程](pic/框架处理用户请求的过程.png)

        WDF框架和WDF驱动是紧密结合在一起的，有很大一部分的重合。“默认分发函数1”表示上面提到的5种命令类型IRP的分发函数，“默认分发函数2”表示上述5种命令类型之外的其他命令类型IRP的分发函数。 
    IO请求参数
        使用DDI接口 WdfRequestGetParameters，可以从 WDFREQUEST对象中获得 WDFREQUEST对象类型相关的结构体
            VOID WdfRequestGetParameters(
                IN WDFREQUEST Request,
                OUT PWDF_REQUEST_PARAMETERS Parameters
            );
        指定一个 WDFREQUEST对象句柄，即可得到一个相关的 WDF_REQUEST_PARAMETERS结构体。
    队列
        在WDM驱动中，会维护一个内核队列，以处理多个同类型的异步请求，比如当读取键盘、鼠标的输入信息时，一个维持一定数量的请求队列能够保证信息不丢失。可以使用 LIST_ENTRY构造双向列表来实现队列，实现这样一个队列算不上一件很容易的事(也可以直接使用 KQUEUE内核对象，简化实现难度)。而 WDF框架借助于队列，让它在IO模型设计中发挥作用，实现对IO请求对象的高效管理。WDF驱动中的队列有3种类型，定义如下
            typedef enum _WDF_IO_QUEUE_DISPATCH_TYPE(
                WdfIoQueueDispatchInvalid=0,
                WdfIoQueueDispatchSequential,
                WdfIoQueueDispatchParallel,
                WdfIoQueueDispatchManual,
                WdfIoQueueDispatchMax
            )WDF_IO_QUEUE_DISPATCH_TYPE;
        在这个枚举类型值种，第一种和最后一种都是无效的，只有中间三种是有效的类型值。第一种是串行队列，队列中的IO请求是一个挨一个被处理的，前一个处理中的对象未完成，后续对象一定不会被处理，串行队列实现了序列化。
        第二种是并行队列，IO请求一旦入队，只要有可能都会以最快的速度被处理，不必等待前面的对象被处理完。
        第三种是手动队列，IO请求入队之后，框架就不会再理会它们，WDF驱动在需要时，自己从队列中提取IO请求并处理
        针对队列可进行Pnp/Power配置，发生Pnp/Power事件时，可配置以什么方式处理队列中的IO请求；还可配置一个Cancel回调，当上层驱动取消相关请求时被调用
        WDF的一个主要特点是，所有的东西都被封装成一个对象，而所有的操作都被定义成一个事件(Event)或回调(Callback)。WDF对每个框架对象都维护一个引用计数，这样就能有效地控制对象的生命周期。
        WDF的一个优点是将I/O进行了封装，使得程序员不用直接面对IRP，而只要处理WDFREQUEST对象即可，处理也变得异常简单。I/O的对象不再是设备对象，而是一个新的I/O target对象。I/O target对象比DEVICE_OBJECT使用更广，它不仅可以代表设备，也可以代表驱动、队列等。队列对象是一个全新事务，WDM编程中涉及队列的地方不多，但却是WDF中不可缺少的部分。队列是专门用来管理 WDFREQUEST对象的，因为 WDFREQUEST是对IRP的封装，所以队列归根到底是对IRP的管理。队列允许 WDFREQUEST对象以3种方式发送给驱动处理：并行、串行、手动。由于对IRP的管理、使用失策而导致的驱动问题，是WDM程序的一大难点。现在队列的引入，让IRP能够良好管理。
        假设有一个用户线程X以同步方式向内核发送一个命令，内核框架收到命令后，判断出命令应当归于串行队列1。此时串行队列1中已经有3个排队命令。用户线程向内核驱动发送一个请求，WDF框架首先获得处理这个请求的机会；此请求隶属于串行队列，WDF便将请求排到串行队列的最后面，作为Request4；线程将一直等待Request4的完成。队列中的前面三个请求处理完成，轮到“新命令”；“新命令”处理结束后，WDF回向通知用户线程，并返回处理结果；内核中的串行队列空(或者继续接受新命令)；线程X继续运行
        每个设备对象都有一个默认队列，未经特殊说明的请求类型都被送往这个默认队列中，如果要把某些请求排列到特殊队列，则需要特殊说明。一般总是把默认队列设置为并行队列，这是为了将效率最大化。只将部分需要特别处理以保证安全的对象放置到串行队列中；而手动队列一般放置一些特殊的请求，这些请求往往是为了等待某个条件被满足以达到同步目的，或等待所需要的数据到来，如从USB的中断端口读取数据。
        多个队列之间可以互相交流，如A队列中的请求，可以被送到B队列中进行排队，这种交流存在于任何两个队列之间。在很多情况下，需要用到队列转移，例如 IRP_MJ_DEVICE_IO_CONTROL类型的请求，一般都可以被并行处理，但控制信号 CTL_CODE为 IOCTL_REQUEST_1的 DEVICE_IO_CONTROL请求却必须被串行处理。可以把 IRP_MJ_DEVICE_CONTROL请求设置为在并行队列中排队，这样绝大部分的控制请求都将被并行处理，而当并行队列的处理函数遇到控制码为 IOCTL_REQUEST_1时，放弃对它的处理，并重新将它送到串行队列中排队等待。
    创建IO请求
        目前框架只对5种IRP请求进行 WDFREQUEST对象封装，但实际上 WDFREQUEST对象可以封装任何一种IRP请求。WDF驱动程序除了使用框架通过事件回调传递的 WDFREQUEST对象外，还可自己新建任何类型的 WDFREQUEST对象。
        创建 WDFREQUEST对象有两种方法。第一种方法是创建空对象，然后调用格式化函数，将对象格式化为指定类型的命令，目前框架只提供了4种格式化函数(共5个函数)，这种方法只能创建4种 WDFREQUEST对象；第二种方法是直接通过一个指定的IRP创建，使用此方法可创建任何类型的 WDFREQUEST对象，根据IRP类型而定。
        调用 WdfRequestCreate创建一个空对象
            NTSTATUS WdfRequestCreate(
                IN OPTIONAL PWDF_OBJECT_ATTRIBUTES RequestAttributes,
                IN OPTIONAL WDFIOTARGET IoTarget,
                OUT WDFREQUEST* Request
            );
        参数RequestAttributes用来配置将被创建的框架对象，这个类型的参数并不是仅针对于 WDFREQUEST对象，所有继承自 WDFOBJECT的框架都使用 WDF_OBJECT_ATTRIBUTES结构体进行对象配置。
        IoTarget是一个可选参数，仅仅用来做验证，并不会被保存到新建的 WDFREQUEST对象中。如果此参数不为NULL，则 WdfRequestCreate函数将验证新建的对象，是否可以被发送到此IO目标对象，如果证实不可能，则 WDFREQUEST对象将创建失败，并返回状态值 STATUS_REQUEST_NOT_ACCEPTED。这个状态值表明，当前系统中的资源不足以创建一个发送到指定IO目标对象的 WDFREQUEST请求
        在成功创建的情况下，参数 Request将返回一个 WDFREQUEST对象句柄。
        成功创建一个空对象，并不能即刻被用，它的内部是“空”的，所以需要格式化，即往对象内部填入表明其“身份”的数据。可用的格式化接口函数有如下4种(5个)
            WdfIoTargetFormatRequestForIoctl
            WdfIoTargetFormatRequestForInternalIoctl
            WdfIoTargetFormatRequestForInternalIoctlOthers
            WdfIoTargetFormatRequestForRead
            WdfIoTargetFormatRequestForWrite
        第一个函数将 WDFREQUEST对象格式化为 IRP_MJ_DEVICE_CONTROL命令；第二、三个函数将对象格式化为 IRP_MJ_INTERNAL_DEVICE_CONTROL命令，这两个函数使用了不同的参数；第四个函数将 WDFREQUEST对象格式化为 IRP_MJ_READ命令；第五个函数将 WDFREQUEST对象格式化为 IRP_MJ_WRITE命令。
            WdfIoTargetFormatRequestForRead(
                IN WDFIOTARGET IoTarget,
                IN OUT WDFREQUEST Request,
                IN OPTIONAL WDFMEMORY OutputBuffer,
                IN OPTIONAL PWDFMEMORY_OFFSET OutputBufferOffset,
                IN OPTIONAL PLONGLONG DeviceOffset
            );
        参数IoTarget指明发送到的IO目标，WDFIOTARGET对象是对 DEVICE_OBJECT对象的封装，最终使用的也恰恰是这个设备对象指针；参数 Request传入一个前面创建的 WDFREQUEST对象句柄，当函数调用成功后，这个对象的内部将焕然一新。
        剩下的3个参数 OutputBuffer、OutputBufferOffset和 DeviceOffset与读操作有关。OutputBuffer代表一个数据缓冲区，用来保存读入的数据。OutputBufferOffset用来指示读数据缓冲区的起始偏移值，如果数据缓冲区中已经放置了一些有用数据，或因其他原因必须保留一部分缓冲区，则应当利用这个偏移值空出头部，这样读缓冲区的长度将是全部长度减去偏移值。DeviceOffset指示目标设备的读偏移值。
        上面三个参数称为“与具体操作相关的参数”，其他的格式化函数与 WdfIoTargetFormatRequestForRead函数的区别之处只在于这些参数。可以通过函数 WdfIoTargetFormatRequestGetParametares获取这些与具体操作相关的参数，这是一个类似于 IO_STACK_LOCATION的结构体。
        第二种创建 WDFREQUEST对象的方法是调用 WdfRequestCreateFromIrp，选择直接从一个已有的IRP结构体进行封装。
            NTSTATUS WdfRequestCreateFromIrp(
                IN OPTIONAL PWDF_OBJECT_ATTRIBUTES RequestAttributes,
                IN PIRP Irp,
                IN BOOLEAN RequestFreesIrp,
                OUT WDFREQUEST* Request
            );
        参数 RequestAttributes是框架对象属性；参数Irp是将要被封装的IRP结构体；参数 RequestFreesIrp用以设置Irp的移除属性，RequestFreesIrp为TRUE，则 WDFREQUEST对象被删除时，将负责调用 IoFreeIrp释放Irp，否则用户必须手动释放它；参数 Request是生成的 WDFREQUEST对象
        WDF驱动创建的 WDFREQUEST对象，必须最后调用 WdfObjectDelete方法进行删除。但如果对象是由框架通过参数传递给 WDF驱动的，则不可调用 WdfObjectDelete方法删除，这个权利应当让给框架在其内部进行。
        发送要求。调用框架接口函数 WdfRequestSend将一个请求发送到指定的IO目标对象。
            BOOLEAN WdfRequestSend(
                IN WDFREQUEST Request,
                IN WDFIOTARGET Target,
                IN OPTIONAL PWDF_REQUEST_SEND_OPTIONS RequestOptions
            );
        第三个参数 RequestOptions。也是一个结构体
            typedef struct _WDF_PWDF_REQUEST_SEND_OPTIONS(
                IN ULONG Size;
                IN ULONG Flags;
                IN LONGLONG Timeout;
            ) WDF_REQUEST_SEND_OPTIONS, *PWDF_REQUEST_SEND_OPTIONS;
        参数Flags是一系列标志值，其中重要的两个标志值是
            WDF_REQUEST_SEND_OPTIONS_SYNCHRONOUS:同步标志。设置同步标志后，直到所发送的请求被完成，WdfRequestSend函数才会返回。请求被完成前，调用者一直处于阻塞状态；如果不设置此标志，则采用相反的异步方式发送请求，WdfRequestSend被调用后将立即返回，而请求完成时，指定的完成函数将被调用。
            WDF_REQUEST_SEND_OPTIONS_TIMEOUT:超时标志。设置超时标志后，框架将把 WDF_REQUEST_SEND_OPTIONS结构体中的TimeOut值作为超时值计算超时。比如，为一个请求设置了1s的超时，如果请求被发送1s后仍未收到完成通知，则框架将取消此请求

### 3.7 PNP和电源类型

    PNP/电源处理代码，较为复杂，分叉路径多。WDF为PNP、电源、电源策略三者定义的状态值。WDF_DEVICE_PNP_STATE、WDF_DEVICE_POWER_STATE和WDF_DEVICE_POWER_POLICY_STATE，三者加起来超过了270个枚举量。按照最严苛的要求，要在驱动中对这些状态都进行处理，哪怕大部分状态只有百万分之一的几率发生。
    WDF开发则相对简单些。
    WDF对电源和PNP的设计方式是，进行最基本的处理，框架向程序提供回调接口，如果程序注册了某个回调，则框架在对象的状态变化时调用此回调，否则就使用默认的处理方式。
    所有的回调函数都是在被动级别上运行，使得程序在进行初始化或反初始化时，不用担心运行于分发级别(DISPATCH_LEVEL)而顾虑重重，因为在分发级别上运行的代码有很多限制，常常免不了要使用WorkItem，而使用WorkItem往往又必须同时实现同步，相当麻烦。
    上述的回调函数和WDM的分发函数之间谈不上一一对应，但也存在着比较强的对应关系。比如函数 EvtDevicePrepareHardware对应了WDM中的 PNP_START_DEVICE分发；函数 EvtDeviceReleaseHardware对应了WDM中的 PNP_STOP_DEVICE分发；函数 EvtDeviceSurpriseRemoval对应了 WDM中的 PNP_SURPRISE_REMOVE分发；函数 EvtDevice0Entry/EvtDeviceD0Exit对应了WDM中的 PNP_SET_POWER分发等。
    在处理 PNP_START_DEVICE时，免不了担心是第几次调用StartDevice函数，考虑电源状态是否已进入D0状态。EvtDevicePrepareHardware回调则不需要考虑，因为框架内部已经做了考虑。

## 4 WDF USB设备驱动开发

### 4.1 USB设备硬件结构

    主从结构
        首先从硬件角度介绍USB，本章的主要内容是介绍内核开发。USB的全称是Universal Serial Bus(通用串行总线)，在硬件上，有两个显著的特点：串行数据传输、支持热插拔
        USB接口自1994年推出以来，经过26年的发展，经过USB1.0/1.1、USB2.0、USB3.x，最终发展到了现在的USB4；传输速率也从最开始的1.5Mbps，大幅提高到了最新的40Gbps。应用遍及各个领域、方方面面。
        USB的另外一个特点是它采用主从结构。两个可以互连的设备，一定有主从之分。这导致了两台主机(Host设备)或者两台从设备(如MP3播放器)之间，没有办法互连，只能在设备(MP3)和主机之间建立主从互连关系。后来出现了OTG协议，可以让设备更换角色，但并未能改变主从结构的本质。
        能称为USB主机，一定要具备两种设备：USB主控制器、USB根集线器。主控制器用来处理根集线器上的数据，交给系统处理；根集线器用来连接多个外部设备，即提供USB埠。不能把这里的根集线器和普通USB集线器画等号，应当把普通的USB集线器也理解为USB外部设备的一种，而非主机的组成部分。
        外设->集线器->控制器->系统。我们使用的每台计算机上有若干个控制器，控制器上有一个或多个根集线器，跟集线器上又对外暴露出一个或多个USB接口(A型接口)让外部设备连接
        每个USB控制器，作为一个USB的核心，其驱动程序负责为子设备分配总线地址。总线地址为7位宽，由于地址0保留，因此最多可提供127个子设备地址，即每个控制器上最多能连接127个子设备，并且这个数目包含了根集线器在内。
        在电器特性方面，标准USB接口有4个金属针脚，对应着USB连接线中的4根金属线：两根电源线、两根数据线。两根金属线，一个接5V电源，一个接地；两根数据线，实现了数据的差分传输，提高了稳定性，等于是一根线。
        对于设备供电，USB设备可以自己供电，也可以从总线获取电源。从总线获取的电源，是通过5V电源线传过来的。例如U盘、键鼠这类小型设备，5V、100mA电流足以满足设备需求，故大多从总线获取电源；移动硬盘、打印机、专业USB声卡等较大设备，往往需要外置电源，以获取更多电力。
    硬件拓扑
        USB设备的拓扑结构可分为三层：硬件总线接口、逻辑设备、多个功能模块。借助这种结构，实现了多种功能集于同一个设备的特点。如USB接口的KVM切换设备(KVM设备上集成了Keyboard、Video和Mouse三种设备接口)
        从自身来看，设备是唯一的，因此对外的接口也是唯一的，对应“总线接口”模块。然后设备存在的目的，是为了完成一定的工作，它能实现多少功能，即表示内部有多少个独立的“功能模块”。多个功能模块同处一个设别，需要有统筹单位来协调资源、总线或时间片，则需要逻辑设备。
    USB中断
        USB的“主从”还有另外一层含义：主机向设备发送命令，设备响应命令；主机如果没有发送命令，设备不能主动联系。即使是在进行输入传输的情况下——设备向主机发送数据——发送数据过程也是在主机的指导下完成的。
        USB中断是“伪中断”。USB设备总是把“中断数据”保存在设备内存中，等待主机来主动索取；如果主机来索取了，就立刻把数据交给它；否则就一直保存着，直到更多新的数据到来时将它覆盖——主机通过这种方式帮助USB设备实现“中断”。
        USB设备的中断端口和批量端口本质上非常像，将批量端口加上主机轮询，差不多也变成一个中断端口。

### 4.2 USB软件结构

    软件结构比硬件结构复杂很多，包含了很多表面上看不到的层次，比如总线驱动、功能驱动、过滤驱动等。
    总线驱动
        总线驱动位于驱动栈的最下层，处理复杂的任务，比如资源分配、子设备管理等。作为下层驱动，负责处理上层驱动发下来的请求。USB设备总线驱动主要有两类：控制器驱动、Hub驱动；另外还有一个端口驱动。
        (1)控制器驱动：Ushohci.sys、Usbuhci.sys、Usbehci.sys
            HCI，代表主机控制接口(Host Control Interface)。历史上共有3中HCI协议出现：USB 1.1，有OHCI(开放型HCI)协议和UHCI(通用HCI)协议；USB 2.0，有EHCI(增强型HCI)协议。
            3个协议分别对应了上面的3个驱动程序。因为USB是向前兼容的，所以Usbehci.sys中也包含了 Usbohci.sys和 Usbuhci.sys的功能
            同一台主机特别是笔记本电脑中，1.1和2.0的控制器并存，例如笔记本电脑中的键盘通过内置USB接口与系统连接，其数据吞吐量小，只需要1.0或1.1的控制器就能满足，而暴露在外供用户使用的接口则需要2.0的控制器。
        (2)Hub驱动：Usbhub.sys
            Hub驱动是所有USB设备的父驱动。
            Hub驱动的子设备要么是独立设备；要么是一个包含多个子设备的父设备。Hub驱动只为直系子设备创建唯一的物理设备对象。Hub驱动为设备1和设备2创建物理设备对象，但并不为设备2的子设备创建物理设备对象

![Hub驱动]()

        (3)端口驱动：Usbport.sys
            这是个框架驱动，比较复杂，很少人会用到。上面的三个驱动都是它的微端口驱动。
    系统类驱动
        出现类驱动，体现了USB总线在应用上的繁荣。
        USB设备包含很多通用的功能类，比如：USB集线器设备、USB HID设别、USB音频设备、USB MIDI设备、USB存储设备。为了让开发工作变得更加简单，Windows操作系统为它们提供了系统驱动程序。
        大多数情况下，系统类驱动就是功能驱动。下表是系统提供的USB类驱动列表

![系统提供的USB类驱动列表]

    功能驱动
        不是所有的USB设备都有类驱动，但功能驱动却是它们唯一的身份证。没有功能驱动，设备就不足以在系统中存在。功能驱动的作用是为设备创建一个独一无二的内核设备对象(DEVICE_OBJECT)以及设备栈，并在需要时，使得系统能通过此设备对象找到它。
        如果要让用户层也能够知道并使用USB设备，功能驱动更不可少。它在用户程序可见的名字空间中为设备起了一个别名，这个别名可以是一个符号链接，也可以是一个由GUID定义的设备Interface(接口)。对这个别名进行操作，也就是对设备本身进行操作。
        而例外是，以RAW模式驱动的设备，这种设备直接由总线驱动来驱动其工作，不需要功能驱动。只有像很底层的控制器设别、Hub设备之类才会这样做。对于RAW模式驱动的设备，当收到 IRP_MN_QUERY_CAPABILITIES查询请求时，在返回的DEVICE_CAPABILITIES结构体中，必须将RawDeviceOK位设置为TRUE
        可以使用WinOBJ.exe工具查看系统空间中的设备与别名。
    父驱动与混合设备
        通过一定的设置，USB设备中的每个接口都可以拥有不同的Class和Protocol定义，从而实现：一个设备，多个功能。这种设备被称为混合设备。混合设备的前提是拥有多个接口，对单接口设备谈“混合”是没有意义的。
        满足如下两个条件的多接口USB设备，被系统认为是混合设备
        (1)在设备描述中，设备类的值为0，即在设备描述符中：(bDeviceClass,bDeviceSubClass,bDeviceProtocol)=(0,0,0)
        (2)具有唯一的配置描述符，即在设备描述符中：(bNumConfigurations)=(1)
        从Windows XP SP2以后，系统还支持另外一种混合设备的判别方式，称作Interface Association Descriptor(IAD)。其实IAD描述符是用来组织“接口组(Interface Group)”的。配置描述符中可以由多个IAD存在，如果将某两个接口组成接口组，首先这两个接口必须紧挨着；其次，必须有一个IAD描述符位于这两个接口描述符的前面，也必须是紧挨着的。IAD描述符中的bFirstInterface用来描述接口组中的第一个接口ID，bInterfaceCount用来描述接口组中包含多少接口。这样，接口集合[bFirstInterface,bFirstInterface+bInterfaceCount]为一个接口组。
        能够用上IAD的设备，一定是有多接口存在的。IAD描述符的识别和实现由通用父驱动完成，有IAD支持的设备都被认为是混合设备。而识别设备中是否有IAD支持，可通过设备描述符中的如下值序列来判断：
            (bDeviceClass,bDeviceSubClass,bDeviceProtocol)=(0xEF,0x02,0x01)
        IAD普及率不是很广，一个原因是Windows XP SP2以后的操作系统才对它给予支持，如果是在Windows XP SP1甚至Windows 2000系统中，此设备可能将被识别为错误的设备，这导致厂商可能不得不提供多套驱动程序。
        当一个多接口混合设备插入计算机后，首先，总线驱动按照常规，读取并分析USB设备描述符，并为其分配如下设备ID：
            USB\VID_vvvv&PID_pppp
            USB\VID_vvvv&PID_pppp&REV_rrrr
            (vvvv,pppp,rrrr)：四位十六进制数，分别代表了厂商ID、产品ID、USB版本，对应于设备描述符中的idVendor/、idProduct/、bcdDevice
        和兼容ID：USB\COMPOSITE
        PNP管理器首先按照常规，根据上述的设备ID（以及总线驱动根据物理位置生成的实例ID）到注册表中为设备寻找合适的驱动程序。如果找到了正确的安装记录，就根据记录中的信息加载驱动程序
        当找不到时，就需要兼容ID，兼容ID“USB\COMPOSITE”在系统中是有注册记录的，并且就对应着通用父设备驱动(Usbccgp.sys)。于是，系统为混合设备加载通用父设备驱动。可以在Windows\Inf目录下查看usb.inf文件，此文件包含了对通用父设备的安装信息
        通用父设备驱动接手后，它就成了子设备的总线驱动，接下来的设备枚举工作就是由它来负责的。通过分析配置描述符，它完成两个动作：首先为每个USB接口（不是USB设备）分配一个设备ID和兼容ID；然后为每个USB接口创建一个物理对象(Physical Device Object)。设备ID形式如下
            USB\VID_vvvv&PID_pppp&MI_mm
            USB\VID_vvvv&PID_pppp&REV_rrrr&MI_mm
        又根据接口描述符中的Class类型分配兼容ID
            USB\CLASS_cc
            USB\CLASS_cc&SUBCLASS_ss
            USB\CLASS_cc&SUBCLASS_ss&PROT_pp
        通用父设备驱动为每个接口创建了物理设备对象后，将接口的设备ID、兼容ID信息提交给PNP管理器，PNP管理器开始为这些“虚假的”物理设备安装驱动。仍然重复上面的过程：根据每个接口的设备ID（以及实例ID）在注册表中搜索，试图找到相关的安装记录，如果找到了，就为接口加载相应的驱动程序；如果找不到，系统就会弹出“发现新设备”对话框，启动驱动安装向导。
        对于多接口的混合设备(Composite Device)，其设备驱动的安装分为两个过程：首先，尝试安装混合驱动，如果找不到，就默认安装通用父设备驱动；然后，通用父设备驱动为每个接口分配设备ID，并分别为每个接口安装驱动程序
        USB混合设备中如果有n个接口，一般情况下对应着n个设备，即n个接口被枚举出n个设备。但当存在接口组时，多个接口被枚举为一个设备：在符合一定条件的情况下，某些接口可以被组合为一个接口组，一个接口组代表一个功能，父设备驱动只为它创建唯一的物理设备对象，并被枚举为唯一的设备。有下面几种组件接口组的方法
            (1)最通用的方法是通过IAD描述符组件接口组，在可能的情况下，此方法应该是最优先考虑的
            (2)最有计数难度的方法是向通用父驱动(Generic father driver)注册厂商回调函数(Vender-Supplied Callback Function)，并在厂商回调函数中拦截父驱动的某些操作，以实现任意组建接口组的目的。因为USB子设备的枚举工作是由通用父驱动实现的，所以只要Hook住通用父驱动并修改其枚举过程中的一些操作，就能达到目的。必须写一个过滤驱动来实现这一目的，这是此方法难以实现的原因所在。但优点是，可以非常有效地把若干个毫无关联的接口组建成接口组
            (3)对于CDC(通信设备类)或者WMCDC(无线移动通信设备类)设备，通用父驱动会自动根据接口的Union Functional Descriptors值为其组建接口组
            (4)音频设备有特殊的定义。如果多个接口具备如下3个条件，通用父驱动将自动为其组件接口组：1.接口ID是连续的；2.接口类都为音频类(bInterfaceClass=1)；3.第一个接口的子类和其他接口的子类不相等。需要注意的是，这种方法的优先级低于IAD
    过滤驱动
        过滤驱动无处不在，很多时候它被称做Hook技术，是一种Hack手段。其实过滤驱动在很多时候都是必不可少的，并被操作系统自身大量使用。过滤驱动可以位于任何一个驱动的上层或下层。过滤的对象也包括已经存在与系统中的其他的过滤的驱动。当过滤驱动位于某层驱动(如D驱动)上面时，所有目标发往D驱动的请求都首先被它截取；当它位于某层驱动(如D驱动)下面时，所有和D驱动相关的从更底层驱动反馈回来的“完成消息”都预先被过滤驱动截取。
    USB驱动栈、设备栈
        驱动栈、设备栈本质上是并行概念。驱动之间的联系是通过设备对象进行的，所以驱动之间是间接联系的，驱动栈也就只是概念上的，它用来表示一个设备能够在系统中被识别、运行，从上到下总共需要哪些驱动程序支持
        设备栈则有据可查，系统中的每个DevNode就表现为一个设备栈
        驱动栈中包含了若干个独立的设备栈，每个驱动可同时存在于若干个不同的设备栈中。

![CY001的驱动栈和设备栈]()

        上图是单接口CY001设备的驱动栈、设备栈全图，也适用于所有其他的单接口USB设备。如果是多接口混合设备，中间就要多一个通用父驱动，稍微复杂一点。
        圆角矩形代表的是一个驱动；里面的直角矩形表示驱动创建的设备。
        最上层是可能存在的过滤驱动，因为只是“可能存在”，所以用虚框表示。其实过滤驱动可以存在于设备栈的任何一个位置，而不仅仅是最上层。
        过滤驱动生成的过滤设备对象，挂载到CY001驱动生成的功能设备对象上；这样所有发送给CY001功能设备对象的请求，过滤设备对象总是先得到。根集线器生成了CY001驱动的物理设备对象。3个设备连在一起，就是CY001驱动程序的设备栈。
        根集线器驱动并不是最底层驱动，必须得到控制器驱动的支持，于是加上可能存在的过滤驱动，形成了中间的设备栈
        USB主机控制器是附载在系统总线上的，在控制器的下面还有若干个驱动层次，包括PCI驱动、ACPI驱动。

### 4.3 内核开发

    设备驱动
        设备驱动和过滤驱动、内核服务不同。后者的存在，可能是为了实现一个内核API的Hook，或者挂载到某个设备以截取数据，目的比较杂、散，但都围绕OS内部。
        设备驱动则目的专一，只是为了让某个物理设备能正常工作，和系统结为紧密的一体
        专一性往往等同于特殊性。拿USB和1394两种设备驱动来说，它们的编程套路，从初始化到设备操作全不一样，这是由设备协议本身决定的：不同的总线、不同的数据格式、不同的传输方式。
        设备驱动需要解决的：设备配置、数据操作、设备控制
            设备配置，即初始化设备。首先能识别到设备，这一点是由下面的总线驱动和PNP管理器搞定的。然后获取设备信息、状态，对USB设备而言，需要知道它的设备描述符、接口数量、端点数量和类型。最后配置设备(设备、PNP、电源、IO等)，并获取必要的系统资源
            数据操作，可被分为两大类：输入和输出。用正确的方法，把正确的数据输入或输出设备，是设备驱动的终极目标。
            设备控制，包括很多操作，因不同类型的设备而异。USB设备控制包括设备Reset、管道Reset、设置特性等
    入口函数
        驱动程序加载由System进程完成，System进程首先在驱动文件的PE结构中寻找入口函数地址，默认的都指向了DriverEntry。虽然名称依旧，但函数实现从WDM跳到WDF框架。
        编写WDM入口程序，主要的工作是初始化驱动对象，还需要创建并初始化一个“控制设备对象”。由于驱动对象和设备对象结构都较大，所以手动初始化的工作很麻烦。
        会导致，即使一个空壳驱动，有大堆的代码需要编写。
        WDF框架，大大减少了代码的书写量，让驱动编程轻松不少。
        WDF的入口函数是这样实现的，用户调用一个接口函数完成驱动程序的默认初始化，默认初始化实现大量的工作，使得用户只要在默认初始化的基础上，略微增加一些自定义设置即可。
            NTSTATUS DriverEntry{
                IN PDRIVER_OBJECT DriverObject,
                IN PUNICODE_STRING RegistryPath
            }(
                WDF_DRIVER_CONFIG config;
                NTSTATUS status = STATUS_SUCCESS;
                WDFWDF_DRIVER_CONFIG_INIT(&config, PnpAdd);
                status = WdfDriverCreate(DriverObject,RegistryPath,WDF_NO_OBJECT_ATTRIBUTES,&config,WDF_NO_HANDLE);
                return status;
            )
        WDF的风格和很多小端口框架很类似。
    USB描述符
        USB协议中的描述符包括：设备描述符、配置描述符、字符串描述符，还有报告(Report)描述符等。了解描述符的最好办法，是读一读USB设备的固件代码。描述符本身是独立的，不受物理设备的约束，只要合乎规矩即可。一个USB设备中最多只能有16个端点，因为端点地址为4bit长。唯一约束着描述符定义的是硬件设计者对物理设备本身的定义，需要多少接口和端点才能实现其需求。
        CY001可以只定义一个接口，对应于开发包中的固件文件CY001(1Interface).hex；也可以定义两个接口，对应于开发包中的固件文件CY001(2Interfaces).hex；当然还可以定义更多的接口，只要不超过256个即可。
    描述符介绍
        USB中的描述符定义有一个共同的特点，就是前两个字节意义相同，其中第一个字节表示结构体的长度，第二个字节表示描述符的类型。描述符对于USB设备非常重要。
        1、设备描述符
            设备描述符总括设备的信息，并提示配置描述符的数量。USB总线驱动在初次发现USB设备时，就是通过获取设备描述符开始其初始化工作的。其中最重要的信息，就在于设备ID(由idVendor和idProduct构成)。下面是设备描述符的定义。
            typedef struct _USB_DEVICE_DESCRIPTOR{
                UCHAR bLength;
                UCHAR bDescriptorType;
                USHORT bcdUSB;
                UCHAR bDeviceClass;
                UCHAR bDeviceSubClass;
                UCHAR bDeviceProtocol;
                UCHAR bMaxPacketSize0;
                USHORT idVendor;
                USHORT idProduct;
                USHORT bcdDevice;
                UCHAR iManufacturer;
                UCHAR iProduct;
                UCHAR iSerialNumber;
                UCHAR bNumConfigurations;
            } USB_DEVICE_DESCRIPTOR, *PUSB_DEVICE_DESCRIPTOR;
        2、配置描述符
            设备可以有多个配置描述符，但一般只有一个；配置描述符中包含了接口描述符；接口描述符中又包含了端点描述符；而接口描述符可根据接口可选值(Alternate Value)而包含多个定义。上述几点都导致了配置描述符的复杂性。配置描述符的定义如下
                typedef struct _USB_CONFIGURATION_DESCRIPTOR{
                    UCAHR bLength;
                    UCHAR bDescriptorType;
                    USHORT wTotalLength;
                    UCHAR bNumInterfaces;
                    UCHAR bConfigurationValue;
                    UCHAR iConfiguration;
                    UCHAR bmAttributes;
                    UCHAR MaxPower;
                } USB_CONFIGURATION_DESCRIPTOR, *PUSB_CONFIGURATION_DESCRIPTOR;
            可以把上述定义理解成描述符的“头”，因为它无法把可能存在的多个接口、端点描述符包含其中。

![配置描述符内部结构]()

            配置描述符(头)领衔，带领它旗下的两个接口(Interface0、1)；每个接口各有两个可选值(0、1)；每个可选值对应于一个接口描述符(方框所示者)；接口描述符的旗下，又有若干个端点描述符(省略号所示)。由此构成了一个完整的配置描述符。端点描述符的定义
                typedef struct _USB_ENDPOINT_DESCRIPTOR{
                    UCHAR bLength;
                    UCHAR bDescriptorType;
                    UCHAR bEndpointAddress;
                    UCHAR bmAttributes;
                    USHORT wMaxPacketSize;
                    UCHAR bInterval;
                } USB_ENDPOINT_DESCRIPTOR,*PUSB_ENDPOINT_DESCRIPTOR;
        3、字符串描述符
            多个字符串描述符是通过ID相区分的。字符串能够以可读形式来描述一样东西，设置可用字符串描述符来描述其他类型的描述符(如设备描述符、配置描述符、接口描述符等)
            描述符ID是从0开始的整数，最多可到0xFF。ID为0的描述符被内部保留，程序不能使用。USB协议允许字符串描述符支持多国语言，ID为0的描述符被专门用来定义语言种类，内部各种语言ID(比如英语ID为0x0904)。在设备内部同一个字符串ID可能会对应着多个字符串描述符。将字符串ID和语言ID加在一起，仍可保证字符串描述符的唯一性。
            字符串描述符在设备固件中定义，数量不限，甚至可以没有。但一般都会包括语言描述符、厂商描述符、产品描述符、序列号描述符。
            字符串描述符定义
                typedef struct _USB_STRING_DESCRIPTOR{
                    UCHAR bLength;
                    UCHAR bDescriptorType;
                    WCHAR bString[1];
                } USB_STRING_DESCRIPTOR;
            固件代码自行组织多个字符串，不在描述符中定义其ID。固件可以把同一个字符串对应于多个ID而返回给系统
        4、其他
            还有一些其他的与特殊类相关的描述符，比如各种类描述符、类的功能描述符(比如Audio类有Audio Streaming描述符，Video类有Video Streaming描述符)；HID设备中的HID描述符、报告描述符；High Speed设备一般会提供OTHER_SPEED_CONFIGURATION描述符，以向前兼容Full Speed模式；仿真USB设备会提供Device Qualifier描述符；支持接口组的设备会提供Interface Associate Descriptor(IAD)描述符等
    读取描述符
        获取设备描述符
            USB_DEVICE_DESCRIPTOR UsbDeviceDescriptor;
            WdfUsbTargetDeviceGetDeviceDescriptor(
                IN pContext->UsbDevice,
                OUT &UsbDeviceDescriptor
            );
        获取配置描述符。配置描述符的特点是，由于内含的接口、端点描述符数量不定，导致它的长度是不定的。首先应取得配置描述符的长度，并根据获得的长度分配内存缓冲区，然后再次获取其内容。
            status = WdfUsbTargetDeviceRetrieveConfigDescriptor(pContext->UsbDevice,NULL,&size);
            if(!NT_SUCCESS(status) && status != STATUS_BUFFER_TOO_SMALL)break;
            if(OutputBufferLength < size)break;
            status = WdfUsbTargetDeviceRetrieveConfigDescriptor(pContext->UsbDevice,pBufferOutput,&size);
        可以对配置描述符做进一步的分析，以获取接口、端点描述符。
        获取字符串描述符。由于字符串描述符是支持多国语言的，所以程序可以通过指定语言ID来获取相应语言的字符串。和配置描述符一样，字符串描述符的长度，也应分两次获取。
    初始化
        DriverEntry调用成功后，驱动文件被加载到系统内存空间，并将开启设备的初始化过程，设备的初始化过程是由PNP管理器主导的。以下是设备接入主机，到设备能够正常工作的完整过程。
            (1)设备插入集线器端口，控制器设备检测到一个高电平信号，知道有新的外设接入设备进来了。这个信号将导致总线驱动注册的ISR(中断服务例程)被调用。总线驱动向设备发送一个复位命令，设备在处理复位操作时，将地址设为0。
            (2)复位成功后，总线驱动继续向设备发送命令，以获取地址描述符。设备描述符的大小是18个字节长，但这次主机只要求获取描述符的前8个字节，目的是得到其中的bMaxPackerSize0值——控制端口的包长度，而协议定义的最小包长度是8个字符
            (3)再次发送复位命令，成功后，将一个有效的非零地址通过Set Address命令发送给设备。如果设置地址成功，则主机以后就通过这个地址和子设备通信
            (4)总线驱动第二次获取设备描述符，这次将获取全部18个字节。通过得到的设备ID，总线驱动将创建一个物理设备对象，并通知内核PNP管理器，从而发起新设备的PNP过程。PNP管理器首先在系统中寻找设备驱动，如果存在匹配驱动则加载之；否则，将引发设备驱动安装过程
            (5)功能驱动在设备初始化的过程中，发送请求获取配置描述符，并根据配置描述符配置设备，称为设备初始化
            (6)设备配置成功后，设备进入工作状态。用户模块将可以与设备进行正常的数据通信
    设备初始化函数
        驱动对象初始化在入口函数，设备对象初始化在AddDevice函数
        入口函数通过一个简单调用完成了驱动初始化。WDF_DRIVER_CONFIG结构体的初始化宏
            WDF_DRIVER_CONFIG_INIT(&config,PnpAdd);
        PnpAdd是一个EvtDriverDeviceAdd类型的回调函数，是AddDevice在WDF中的替身。也是在设备初始化的过程中，第一个被框架调用的回调函数。此时设备还处于枚举过程，设备栈尚未建立。在PnpAdd中完成：
            (1)创建框架设备对象
            (2)创建设备对象的符号链接或设备接口，供用户程序似乎用
            (3)创建框架队列
            (4)创建驱动对象的接口，供其他驱动程序使用
            (5)初始化WMI接口。
        和AddDevice不同的是，PnpAdd在被调用之前，框架已经做了很多事情，包括创建WDM功能设备对象(即DEVICE_OBJECT对象)；初始化 WDFDEVICE_INIT结构体，这个结构体非常重要。EvtDriverDeviceAdd的函数声明
            typedef NTSTATUS(*PFN_WDF_DRIVER_DEVICE_ADD)(
                IN WDFDRIVER Driver,
                IN PWDFDEVICE_INIT DeviceInit
            );
        第一个参数是驱动对象，即 DriverEntry函数中被初始化的对象
        第二个参数是 WDFDEVICE_INIT结构体。它涉及了设备配置的电源、PNP、电源策略、文件、I/O等方面。
        WDFDEVICE_INIT结构体的初始化API可分为三类：对应于普通设备对象(Device)的初始化、专门针对功能设备对象(FDO)的初始化和专门针对物理设备对象(PDO)的初始化
        三类API的数据加在一起，总共约40个。设备驱动只用到了前两类，第三类API属于底层的总线驱动使用。
        设备安装类是在设备安装时由安装文件(INF文件)静态指定的，驱动创建的设备对象，在PNP管理器的管理下都会归入这个安装类下。安装类由一个可读名称和一个GUID值指定。
        调用 WdfDeviceInitSetDeviceClass函数，并传入正确的代表其他设备类的GUID，就可以修改为其他设备类别。
        通过WdfFdoInitQueryXXX函数可以直接获取很多设备信息，比如物理设备对象、硬件键路径、软件键路径、设备ID、设备类等
        所有初始化API都必须在 WdfDeviceCreate之前被调用。一旦 WdfDeviceCreate被调用，框架就收回对 WDFDEVICE_INIT结构体的控制权了，功能驱动如果继续使用，将面临使用无效指针的危险。
    创建设备对象
        设备对象是最基本的内核对象之一。设备对象未必都对应于一个物理设备，而“物理设备对象”也未必真的对应于一个物理外设。大多数情况下，设备只是一个逻辑概念，或者只是一个内核结构体。
        但系统通过操作这些对象，最终达到控制物理设备的目的
        除了 WDFDEVICE外，WDF框架还专门针对USB设备对象进一步封装了一个称作 WDFUSBDEVICE的对象，可以称为 WDF USB设备对象，是对最原始的DEVICE_OBJECT对象的两层封装
        在驱动中，要先后创建 WDFDEVICE对象和 WDFUSBDEVICE对象。WDFDEVICE是由框架负责管理的，WDFUSBDEVICE则完全由驱动程序管理，所以要找一个地方把它保存起来。WDF框架为所有的对象都设计了“环境变量”，还可以在这里面保存私有数据。
    设备命名、符号链接
        和WDM驱动一样，设备对象是可以选择被命名的，也可以选择不命名，由程序员自己决定。命名的目的是为了能够被其他程序识别并使用。
        功能设备对象总是需要命名的，因为功能设备对象被用户程序用来和内核交互。
        通过判断WdfDeviceCreate调用返回的错误值是否为 STATUS_OBJECT_NAME_COLLISION，可以知道当前尝试的名称在系统中是否引起了名字冲突。如果发生冲突，就需要重新尝试。
        一旦命名成功，就可以使用WinOBJ在Device目录下查看此设备。接下来为设备创建符号链接(或设备接口)，这样用户程序也能够看到并使用这个设备
        符号链接和设备对象一样，也是内核对象的一种。调用WdfDeviceCreateSymbolicLink创建符号链接，其参数是设备句柄和符号链接名。系统将因此创建一个符号链接内核对象，并指向设备句柄所代表的设备对象的名称。
            nLen = wcslen(wcsDosDeviceName);
            wcsDosDeviceName[nLen-1] += nInstance;
            status = WdfDeviceCreateSymbolicLink(device, &DosDeviceName);
        设备接口也是符号链接，但命名方式更复杂。它首先根据接口GUID为设备创建接口类(如果已存在则不会创建)，然后在接口类下创建接口实例。在驱动程序中创建设备接口和创建符号链接，有一个非常明显的区别：符号链接的目标对象是功能设备对象，而设备接口的目标对象是物理设备对象(二者位于同一个设备栈)。
        GUID能最大限度地保证唯一性。另外，设备接口还具有一个特点，即可以被启动和禁止。如此，设备接口有三个优点：第一，具有COM接口属性，可以通过COM接口方式引用；第二，内核驱动加强了对暴露给用户程序的设备接口的管理，可以随时启用、禁止；第三，由于是基于GUID的，因此再多的设备接口也不会重名
        调用函数 WdfDeviceCreateDeviceInterface完成接口创建
            NTSTATUS WdfDeviceCreateDeviceInterface(
                IN WDFDEVICE Device,
                IN CONST GUID* InterfaceClassGUID,
                IN OPTIONAL PCUNICODE_STRING ReferenceString
            );
        这个函数被调用时，系统会首先到注册表中检查InterfaceClassGUID所代表的接口类是否已注册，如果没有注册就先注册；然后在这个接口类下创建一个设备接口实例，这个接口实例名称由系统决定，这个名称包含了三部分：接口类GUID(字符串)、可选的引用字符串，以及设备ID的一部分
        首先定义一个GUID，可以使用GUID Generator工具。
        然后开始创建设备接口
        接口实例可以被启动和禁止，这是通过WdfDeviceSetDeviceInterfaceState调用实现的。接口实例在上面被创建时，默认就已经启动了。当系统发生异常，比如设备长时间不能响应时，驱动可选择禁止接口实例
        在驱动中同时创建符号链接和设备接口实例是没有问题的，二者都可以通过WinOBJ和SymLinks工具查看，但在查看设备接口实例之前，首先要到注册表DeviceClass键下找到它的名字才行。
    启动设备
        在WDM驱动中AddDevice调用成功后，PNP管理器会紧接着发送给子命令为PNP_MN_START_DEVICE的IRP_MJ_PNP请求，WDM模式的设备驱动会为这个请求定义一个名称类似于StartDevice的处理函数
        EvtDevicePrepareHardware回调函数在WDF中扮演 StartDevice
        EvtDevicePrepareHardware是驱动初始化过程中，紧接着 EvtDriverDeviceAdd第二个被框架调用的回调函数。此时 EvtDeviceD0Entry尚未被调用，即设备尚未真正进入D0状态，一切针对设备的I/O操作尚不能进行
        EvtDevicePrepareHardware的任务就是为设备申请必要的系统资源，为以后的设备操作做好准备。在自己定义的 EvtDevicePrepareHardware中完成：配置设备，设置电源策略，获取总线接口，枚举系统资源，前两个最重要
        1、接口配置
            在WDM驱动中完成设备配置是一件苦差事。用WDF框架却简单至极，配置设备的顺序是：首先选择配置描述符，然后设置接口可选值。
            WDF框架对第一项任务“选择配置描述符”做了极大的简化。WDF框架默认选择第一个配置描述符为当前配置，这个操作在PnpPrepareHardware函数被调用前就已完成，如果不需要切换到其他配置描述符，那么驱动就可以什么都不做。在绝大多数情况下，USB设备总是选择第一个配置描述符为当前配置，所以绝大多数WDF驱动就再也不必为配置描述符操心了。
            接口总是需要配置的。接口配置分两种情况：单接口配置和多接口配置。为了编程方便，WDF为不同种类的接口配置定义了多个宏。配置多接口的宏也可以用来配置单接口，当把多接口的“多”设为“1”时，也就成了单接口。
                numInterfaces = WdfUsbTargetDeviceGetNumInterfaces(DeviceContext->UsbDevice);
                if(numInterfaces == 1){
                    WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE(&usbConfig);
                }
                else{
                    settingPairs = ExAllocatePoolWithTag(PagedPool,
                    sizeof(WDF_USB_INTERFACE_SETTING_PAIR)*numInterfaces,POOLTAG);
                    if(settingPairs == NULL)
                        return STATUS_INSUFFICIENT_RESOURCES;
                    InitSettingPairs(DeviceContext->UsbDevice,settingPairs,2);
                    WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES(&usbConfig,2,settingPairs);
                }
                status = WdfUsbTargetDeviceSelectConfig(DeviceContext->UsbDevice,WDF_NO_OBJECT_ATTRIBUTES,&usbConfig);
            usbConfig变量是一个WDF_USB_DEVICE_SELECT_CONFIG_PARAMS结构体指针，称为USB配置参数块。结构体内部含有4个结构体组成的联合(union)，对应于不同场合下的设备配置。也可以通过这个结构体进行反配置操作。有5个初始化宏用来对这个结构体进行初始化设置，其中4个与配置操作有关，1个与反配置操作有关。
            在4个配置宏中，WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE 和 WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES 在上面讲述过。
            WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS：这个宏较为复杂，要求用户从配置描述符析取全部的接口描述符。析取接口描述符的方式：
                (1)调用 WdfUsbTargetDeviceGetInterface获取接口句柄。
                (2)调用 WdfUsbInterfaceGetDescriptor获得接口描述符
                (3)循环执行步骤1~2，直到取得全部描述符。描述符的个数可通过函数 WdfUsbTargetDeviceGetNumInterfaces获取
            WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_URB：这个宏实现对WDM的兼容，其参数是一个类型为_URB_SELECT_CONFIGURATION的URB结构体。很少会用到这个宏，它却是解决前文件讲到的在WDF框架中进行配置切换问题的最佳方法。
            上面代码在进行多接口配置时用到函数 InitSettingPairs，其作用是初始化 WDF_USB_INTERFACE_SETTING_PAIR结构体
            关于接口组，一般情况是USB设备一个接口组对应于一个功能，一个功能对应一个驱动程序。但也存在一些情况是一个接口无法完美表现一个独立功能，要想办法把多个接口组合在一起，才能把某个功能表现完成。例如，USB音频设备，一个设备能够提供多通道音视频接口，如果因此而认为它有多个功能模块，必须为每个接口独立编写驱动程序，就太麻烦了
            将多个接口组成接口组(Interface Collection)实现一个共同的功能，系统用唯一的驱动程序来驱动它，这给软件设计带来极大的便利。
        2、设置电源能力和策略
            设备的“电源能力”，即设备在电源控制上可达到的能力；而电源策略，则是对于这些设备具有的“电源能力”，驱动程序具体的实现“策略”
            KMDF总功能支持的电源能力是有限的
                (1)D0和D3两种电源状态是驱动和设备必须支持的，D1和D2则可选（默认不支持）
                (2)当设备进入休眠状态后，在何种情况下可被唤醒。比如，最低在D1状态下，设备可被唤醒；当设备进入D2和D3状态后，即无法唤醒，只能重新上电枚举
                (3)系统电源状态Sx与设备电源状态Dx之间的映射
                (4)系统进入休眠状态时，设备可将系统唤醒；但有两个电源状态阈值：系统最低可被唤醒电源状态和设备最低可发送唤醒信号状态。比如，系统能被唤醒的最低电源状态为S2，那么在S3状态下设备无法唤醒系统；设备只有在D1状态下才能唤醒系统，那么当设备处于D3状态时，将无法把系统唤醒
                (5)当设备进入休眠状态后，隔一定时间系统可以自动将设备唤醒。比如，如果设备长时间没有被使用，则自动休眠，系统检测到此状态变迁后，就开始计时，如果1分钟后设备仍然在休眠，就将它唤醒；此1分钟即“系统自动唤醒延时”
                (6)当系统进入休眠状态时(发生状态变迁)，设备将进入何种电源状态(设备被动发送状态变迁)。比如，将CY001连接在笔记本电脑上(D0)，用户将笔记本电脑盖子合上，电脑将进入S4状态，CY001也将离开D0状态，但具体进入何种休眠状态，需在电源策略中设置
            WDF_DEVICE_POWER_CAPABILITIES结构体对电源能力的定义
                typedef struct _WDF_DEVICE_POWER_CAPABILITIES{
                    ULONG Size;
                    WDF_TRI_STATE DeviceD1; // 是否支持D1、D2状态
                    WDF_TRI_STATE DeviceD2; // True为支持
                    WDF_TRI_STATE WakeFromD0; // D0本身为醒着，但仍可以接受一个Wake信号
                    WDF_TRI_STATE WakeFromD1; // D1可被唤醒
                    WDF_TRI_STATE WakeFromD2;
                    WDF_TRI_STATE WakeFromD3;
                    DEVICE_POWER_STATE DeviceState[PowerSystemMaximum]; // Sx与Dx之间的映射
                    DEVICE_POWER_STATE DeviceWake; //设备的最低状态
                    SYSTEM_POWER_STATE SystemWake; //系统的最低状态
                    ULONG D1Latency; //系统主动唤醒设备
                    ULONG D2Latency;
                    ULONG D3Latency;
                    DEVICE_POWER_STATE IdealDxStateForSx;
                } WDF_DEVICE_POWER_CAPABILITIES, *PWDF_DEVICE_POWER_CAPABILITIES;
            闲时休眠，是指如果USB设备在一定时间内一直没有工作，就据此判断在接下来更长的时间内，也不会有实际工作需要做，则自动进入休眠状态以节约能量；而远程唤醒是指设备进入休眠状态后，通过软件或硬件上的操作，使其恢复到工作状态
            闲时休眠用到一个关键结构体，WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS
            函数 WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT用来对此结构体进行初始化
                VOID WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT(
                    OUT PWDF_DEVICE_POWER_POLICY_IDLE_SETTINGS Settings,
                    WDF_POWER_POLICY_S0_IDLE_CAPABILITIES IdleCaps
                );
            第二个参数是一个枚举型变量，注释写为“自唤醒能力”，它表示设备所具有的这样一种能力：设备进入休眠状态后，在系统仍处于S0状态的情况下，设备是否有能力将自己唤醒。IdleCannotWakeFromS0表示不能；IdleCanWakeFromS0表示能；值IdleUsbSelectiveSuspend它代表了USB设备的选择性挂起(Selective Suspend)能力，用于USB集线器设备，让连接到集线器的部分设备进入休眠状态，区别于全部休眠(Global Suspend)，USB设备若支持自唤醒能力，必须设置此值(MSDN中指明，不可设置为 IdleCanWakeFromS0)
            另外，需要设置闲置(Idle)时间，即设备多长时间不被使用就进入休眠状态。idleTimeOut以毫秒为单位，如果设置闲暇时间为10s，则应将idleTimeOut赋值为10000。
            再看远程唤醒。远程唤醒包含了唤醒设备自身和唤醒系统两个方面。
            进入休眠状态后，软件或硬件的任何操作都能将它唤醒；如果设备休眠后主机也能进入休眠状态，则通过硬件上的操作可令设备和系统同时醒来。
            远程唤醒用到了结构体 WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT，定义如下
                typedef struct _WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS{
                    ULONG Size;
                    DEVICE_POWER_STATE DxState;
                    WDF_POWER_POLICY_SX_WAKE_USER_CONTROL UserControlOfWakeSettings;
                    WDF_TRI_STATE Enabled;
                } WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS;
            DxState是上面讲到的第六项电源能力：当系统进入休眠状态后，设备的电源状态。可取D1~D3，但不可能为D0，因为如果系统已经休眠了，连接到系统上的硬件设备不可能仍处于工作状态。在默认情况下，DxState被设置为DevicePowerMaximum，系统将根据实际情况自行设定它。
            Enabled设置是否允许设备唤醒系统
            UserControlOfWakeSettings和Enabled值有关，它用来设置用户对“设备唤醒系统能力”的控制，用户可通过在注册表中的设置来改变Enabled值所确定的电源唤醒策略。在默认情况下这是允许的
            关于电源的状态映射。设备可拥有多种电源状态：D0~D3；数字越大，代表的电源量越少。D0为完全工作状态，D3为断电状态，设备必须支持D0和D3两种状态；D1、D2状态由设备或总线自定义，可选
            设备电源状态之间的变迁有一个规则，以Dx代表D1~D3来讲述。这个规则是：状态变迁只有两个方向，即D0->Dx，或者Dx->D0；直接在Dx之间变迁是不行的。
            原因是：在休眠甚至断电状态下访问、改变硬件配置是被禁止的，必须先回到工作状态D0才行。处于Dx状态下的设备，没有能力把自己的电源状态直接转换到另一种Dx状态
            系统的电源状态：S0为完全工作状态，S1~S3为休眠状态，S4为待机状态，S5为断电状态（数字越大，代表的电源量越少）
            系统状态是全局的，设备状态是个别的，需要有一个映射：当系统电源处于Sx状态时，设备电源应当处于什么状态(Dx)。
        3、选择性挂起(Selective Suspend)
            选择性挂起是相对全局性挂起而言的。也就是USB Hub设备有能力只让某些端口上连接着的设备进入休眠状态(停止供电)，而令其他端口上的设备仍处于工作状态(保持供电)。这种能力在USB 2.0协议中被提出，并从Windows XP系统开始被支持
            好处是节约了电能。事实是：只要Hub上有一个设备仍处于工作状态，系统就不能进入休眠状态。
            USB设备驱动有两种方式可进入选择性挂起状态：发布电源设置请求 IRP_MN_SET_POWER；发布idle请求(IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION)。选择何种方式取决于操作系统版本和设备本身。
            对于混合设备，如果支持系统对设备的远程唤醒(发布 IRP_MN_WAIT_WAKE请求)，则只能通过发布idle请求以进入选择性挂起状态
            对于操作系统版本的区别，只有Windows XP及以后的系统才支持此特性；在Windows XP下只能使用idle请求；在Windows Vista下二者都可以
            WDF的实现较为简单，只需要设置支持选择性挂起，框架就会自动在内部运行计时检查。设备驱动程序在一段时间内没有收到任何用户操作，就向总线驱动请求将设备挂起，并设置一个回调函数，只要总线驱动判断设备可以安全进入低电源状态，就调用此回调函数来通知设备驱动。设备驱动在回调函数中做休眠前的善后工作
            idle请求发送到总线后，通过返回值的判断可知总线驱动的决定。如果总线驱动经审定认为设备可以被安全地挂起，那么设备将就此进入休眠状态
    创建队列*
    停止设备/反初始化
        


