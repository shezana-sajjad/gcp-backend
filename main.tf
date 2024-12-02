provider "google" {
  project = "cloud-resume-shezana"
  region  = "us-central1"
}

resource "google_cloudfunctions_function" "visitor_counter" {
  name                  = "count-func02"             
  runtime               = "python311"                 
  entry_point           = "counter"           
  source_archive_bucket = "shezana.online"
  source_archive_object = "cloud-resume-terraform.zip" 
  trigger_http          = true                        
}
