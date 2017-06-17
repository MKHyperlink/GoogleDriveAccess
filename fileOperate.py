from apiclient import errors


def get_file(service, file_id):
  return service.files().get(fileId=file_id).execute()

def print_file(service, file_id):
  """Print a file's metadata.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to print metadata for.
  """
  try:
    file = service.files().get(fileId=file_id).execute()

    print 'Title: %s' % file['title']
    print 'MIME type: %s' % file['mimeType']
  except errors.HttpError, error:
    print 'An error occurred: %s' % error


def download_file(service, drive_file, gid):
  """Download a file's content.

  Args:
    service: Drive API service instance.
    drive_file: Drive File instance.

  Returns:
    File's content if successful, None otherwise.
  """
  # download_url = drive_file.get('downloadUrl')
  download_url = drive_file.get('exportLinks').get('text/csv')
  download_url = "%s&gid=%s" %(download_url, gid)
  print download_url
  if download_url:
    resp, content = service._http.request(download_url)
    if resp.status == 200:
      print 'Status: %s' % resp
      return content
    else:
      print 'An error occurred: %s' % resp
      return None
  else:
    # The file doesn't have any content stored on Drive.
    return None

def save_file(content, path):

  if not os.path.exists(os.path.dirname(path)):
    try:
        os.makedirs(os.path.dirname(path))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

  text_file = open(path, "w")
  text_file.write(content)
  text_file.close()
