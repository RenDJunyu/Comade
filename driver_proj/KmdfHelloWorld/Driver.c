/*
*******************************************************************************
*= = �ļ����ƣ�HelloDRIVER.c
*= = �ļ���������������HelloDRIVER����
*= = ��    �ߣ������辶
*= = ��дʱ�䣺2009-04-23 21:16:00
*******************************************************************************
*/

#include "HelloDRIVER.h" 
#include <wdf.h>
#include <wdfobject.h>

//*============================================================================ 
//*= = Ԥ������ 
//*============================================================================ 

#pragma alloc_text(INIT, DriverEntry)
#pragma alloc_text(PAGE, DefaultDispatch)
#pragma alloc_text(PAGE, DriverUnload)

WdfRequestProbeAndLockUserBufferForWrite()

//*============================================================================
//*= = �������ƣ�DriverEntry
//*= = ��������������������ں��� 
//*= = ��ڲ�����PDRIVER_OBJECT, PUNICODE_STRING 
//*= = ���ڲ�����NTSTATUS
//*============================================================================

NTSTATUS
DriverEntry(
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

    // ������ǲ���� 
    for (i = 0; i <= IRP_MJ_MAXIMUM_FUNCTION; i++)
    {
        DriverObject->MajorFunction[i] = DefaultDispatch;
    }

    DriverObject->DriverUnload = DriverUnload;
    DriverObject->MajorFunction[IRP_MJ_CREATE] = DefaultDispatch;
    DriverObject->MajorFunction[IRP_MJ_CLOSE] = DefaultDispatch;
    DriverObject->MajorFunction[IRP_MJ_READ] = DefaultDispatch;
    DriverObject->MajorFunction[IRP_MJ_WRITE] = DefaultDispatch;

    // �����豸 
    status = IoCreateDevice(DriverObject,
        sizeof(DEVICE_EXTENSION),
        &deviceName,
        FILE_DEVICE_UNKNOWN,
        0,
        TRUE,
        &deviceObject);
    if (!NT_SUCCESS(status))
    {
        return status;
    }

    deviceObject->Flags = DO_BUFFERED_IO;
    deviceExtension = (PDEVICE_EXTENSION)deviceObject->DeviceExtension;
    deviceExtension->DeviceObject = deviceObject;
    deviceExtension->DeviceName = deviceName;

    RtlInitUnicodeString(&symbolicLink, L"\\??\\HelloDRIVER");
    deviceExtension->SymbolicLink = symbolicLink;

    // ������������ 
    status = IoCreateSymbolicLink(&symbolicLink, &deviceName);

    if (!NT_SUCCESS(status))
    {
        IoDeleteDevice(deviceObject);
        return status;
    }

    KdPrint(("End of HelloDRIVER DriverEntry!\n"));
    return status;
}

//*============================================================================
//*= = �������ƣ�DriverUnload 
//*= = ������������������ж�غ��� 
//*= = ��ڲ�����PDRIVER_OBJECT 
//*= = ���ڲ�����VOID 
//*============================================================================

VOID
DriverUnload(
    __in PDRIVER_OBJECT DriverObject
)
{
    PDEVICE_OBJECT deviceObject;
    UNICODE_STRING linkName;
    KdPrint(("Enter HelloDRIVER DriverUnload!\n"));

    deviceObject = DriverObject->DeviceObject;

    while (NULL != deviceObject)
    {
        PDEVICE_EXTENSION deviceExtesion =
            (PDEVICE_EXTENSION)deviceObject->DeviceExtension;

        // ɾ�������������豸
        linkName = deviceExtesion->SymbolicLink;
        IoDeleteSymbolicLink(&linkName);
        deviceObject = deviceObject->NextDevice;
        IoDeleteDevice(deviceExtesion->DeviceObject);
    }

    KdPrint(("End of HelloDRIVER DriverUnload!\n"));
}

//*============================================================================
//*= = �������ƣ�DefaultDispatch 
//*= = ������������������Ĭ����ǲ���� 
//*= = ��ڲ�����PDEVICE_OBJECT, PIRP 
//*= = ���ڲ�����NTSTATUS
//*============================================================================

NTSTATUS
DefaultDispatch(
    __in PDEVICE_OBJECT DeviceObject,
    __in PIRP Irp
)
{
    NTSTATUS status;
    KdPrint(("Enter HelloDRIVER DefaultDispatch!\n"));

    UNREFERENCED_PARAMETER(DeviceObject);
    status = STATUS_SUCCESS;

    // ���IRP���� 
    Irp->IoStatus.Status = status;
    Irp->IoStatus.Information = 0;
    IoCompleteRequest(Irp, IO_NO_INCREMENT);

    KdPrint(("End of HelloDRIVER DefaultDispatch!\n"));
    return status;
}

//*============================================================================
//*= = �ļ����� 
//*============================================================================
