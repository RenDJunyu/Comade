// driver.c
#include <ntddk.h>

void DriverUnload(PDRIVER_OBJECT pDriverObject);

NTSTATUS DriverEntry(PDRIVER_OBJECT pDriverObject, PUNICODE_STRING pRegPath)
{
	DbgPrint("[MyDriver] DriverEntry\n");
	NTSTATUS status = STATUS_SUCCESS;
	pDriverObject->DriverUnload = DriverUnload;

	return status;
}

void DriverUnload(PDRIVER_OBJECT pDriverObject)
{
	DbgPrint("[MyDriver] DriverUnload\n");

	return;
}
