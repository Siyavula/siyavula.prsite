#!/bin/bash

rm -rf var/filestorage/*
rm -rf var/blobstorage/*
cp backup/Data.fs var/filestorage/
cp -r backup/blobstorage/* var/blobstorage/
