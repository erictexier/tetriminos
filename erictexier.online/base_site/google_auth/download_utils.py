# -*- coding: utf-8 -*-

import io
from googleapiclient.http import MediaIoBaseDownload


def download_doc_file(drive_service, file_id, output_file):

    request = drive_service.files().export_media(
                                      fileId=file_id,
                                      mimeType="application/rtf")

    fh = open(output_file, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    fh.close()


def download_pdf_file(drive_service, file_id, output_file):

    request = drive_service.files().get_media(fileId=file_id)

    fh = open(output_file, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    fh.close()
