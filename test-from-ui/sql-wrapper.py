# Databricks notebook source
spark.sql(dbutils.widgets.get('sql_statement'))
