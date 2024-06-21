$certname = "test_app_cert"    ## Replace {certificateName}
$exp_date = Get-Date -Year 2026
$cert = New-SelfSignedCertificate `
  -Subject "CN=$certname" `
  -CertStoreLocation "Cert:\CurrentUser\My" `
  -KeyExportPolicy Exportable `
  -KeySpec Signature `
  -KeyLength 4096 `
  -KeyAlgorithm RSA `
  -HashAlgorithm SHA256 `
  -NotAfter $exp_date
Export-Certificate `
  -Cert $cert `
  -FilePath "C:\Users\IANovikov\Projects\outlook_calendar\certs\$certname.cer"
