{{/*
Expand the name of the chart.
*/}}
{{- define "calipsoplus-portal.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" }}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If release name contains chart name it will be used as a full name.
*/}}
{{- define "calipsoplus-portal.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{- .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" }}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "calipsoplus-portal.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" }}
{{- end }}

{{- /*
  calipsoplus-portal.appLabel:
    Used by "calipsoplus-portal.labels".
*/}}
{{- define "calipsoplus-portal.appLabel" -}}
{{ .Values.nameOverride | default .Chart.Name | trunc 63 | trimSuffix "-" }}
{{- end }}


{{- /*
  calipsoplus-portal.componentLabel:
    Used by "calipsoplus-portal.labels" and "calipsoplus-portal.nameField".

    NOTE: The component label is determined by either...
    - 1: The provided scope's .componentLabel
    - 2: The template's filename if living in the root folder
    - 3: The template parent folder's name
    -  : ...and is combined with .componentPrefix and .componentSuffix
*/}}
{{- define "calipsoplus-portal.componentLabel" -}}
{{- $file := .Template.Name | base | trimSuffix ".yaml" -}}
{{- $parent := .Template.Name | dir | base | trimPrefix "templates" -}}
{{- $component := .componentLabel | default $parent | default $file -}}
{{- $component := print (.componentPrefix | default "") $component (.componentSuffix | default "") -}}
{{ $component }}
{{- end }}

{{- /*
  calipsoplus-portal.commonLabels:
    Foundation for "calipsoplus-portal.labels".
    Provides labels: app, release, (chart and heritage).
*/}}
{{- define "calipsoplus-portal.commonLabels" -}}
app: {{ .appLabel | default (include "calipsoplus-portal.appLabel" .) }}
release: {{ .Release.Name }}
{{- if not .matchLabels }}
chart: {{ .Chart.Name }}-{{ .Chart.Version | replace "+" "_" }}
heritage: {{ .heritageLabel | default .Release.Service }}
{{- end }}
{{- end }}

{{- /*
  calipsoplus-portal.labels:
    Provides labels: component, app, release, (chart and heritage).
*/}}
{{- define "calipsoplus-portal.labels" -}}
component: {{ include "calipsoplus-portal.componentLabel" . }}
{{ include "calipsoplus-portal.commonLabels" . }}
{{- end }}


{{/*
Selector labels
*/}}
{{- define "calipsoplus-portal.selectorLabels" -}}
app.kubernetes.io/name: {{ include "calipsoplus-portal.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- /*
  calipsoplus-portal.matchLabels:
    Used to provide pod selection labels: component, app, release.
*/}}
{{- define "calipsoplus-portal.matchLabels" -}}
{{- $_ := merge (dict "matchLabels" true) . -}}
{{ include "calipsoplus-portal.labels" $_ }}
{{- end }}

{{/*
Create the name of the service account to use
*/}}
{{- define "calipsoplus-portal.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (include "calipsoplus-portal.fullname" .) .Values.serviceAccount.name }}
{{- else }}
{{- default "default" .Values.serviceAccount.name }}
{{- end }}
{{- end }}

{{- define "imagePullSecret" }}
{{- with .Values.imagePullSecrets }}
{{- printf "{\"auths\":{\"%s\":{\"username\":\"%s\",\"password\":\"%s\",\"email\":\"%s\",\"auth\":\"%s\"}}}" .registry .username .password .email (printf "%s:%s" .username .password | b64enc) | b64enc }}
{{- end }}
{{- end }}
