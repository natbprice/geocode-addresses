# Load modules
import ftputil
import zipfile

# Output directory
outDir = "E://QGIS//"

# Download files
with ftputil.FTPHost("ftp2.census.gov", "anonymous", "") as ftp_host:
    # Download place shapefiles
    ftp_host.chdir("/geo/tiger/TIGER2018/PLACE/")
    names = ftp_host.listdir(ftp_host.curdir)
    for name in names:
        if ftp_host.path.isfile(name):
            print("Downloading:" + name)
            ftp_host.download(name, outDir + "tl_2018_place//" + name)
            print("Unzipping:" + name)
            zip_ref = zipfile.ZipFile(outDir + "tl_2018_place//" + name, 'r')
            zip_ref.extractall(outDir + "tl_2018_place//")
            zip_ref.close()

    # Download address feature shapefiles
    ftp_host.chdir("../ADDRFEAT/")
    names = ftp_host.listdir(ftp_host.curdir)
    for name in names:
        if ftp_host.path.isfile(name):
            print("Downloading:" + name)
            ftp_host.download(name, outDir + "tl_2018_addrfeat//" + name)
            print("Unzipping:" + name)
            zip_ref = zipfile.ZipFile(outDir + "tl_2018_addrfeat//" + name, 'r')
            zip_ref.extractall(outDir + "tl_2018_addrfeat//")
            zip_ref.close()

    # Download county shapefiles
    ftp_host.chdir("../COUNTY/")
    names = ftp_host.listdir(ftp_host.curdir)
    for name in names:
        if ftp_host.path.isfile(name):
            print("Downloading:" + name)
            ftp_host.download(name, outDir + "tl_2018_us_county//" + name)
            print("Unzipping:" + name)
            zip_ref = zipfile.ZipFile(outDir + "tl_2018_us_county//" + name, 'r')
            zip_ref.extractall(outDir + "tl_2018_us_county//")
            zip_ref.close()

    # Download ZCTA shapefiles
    ftp_host.chdir("../ZCTA5/")
    names = ftp_host.listdir(ftp_host.curdir)
    for name in names:
        if ftp_host.path.isfile(name):
            print("Downloading:" + name)
            ftp_host.download(name, outDir + "tl_2018_us_zcta510//" + name)
            print("Unzipping:" + name)
            zip_ref = zipfile.ZipFile(outDir + "tl_2018_us_zcta510//" + name, 'r')
            zip_ref.extractall(outDir + "tl_2018_us_zcta510//")
            zip_ref.close()

