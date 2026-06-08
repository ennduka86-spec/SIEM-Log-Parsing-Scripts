Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624,4625} |
  Select-Object TimeCreated, Id, Message |
  Export-Csv parsed_events.csv -NoTypeInformation
