from django.shortcuts import render
from django.http import HttpResponse
from app.models import Details, History_operation, Stages, Work_pieces


def details(request):
    columns_details = Details.objects.values_list(
        "id", "name", "type", "created_at", "updated_at"
    )
    html = ""
    for id_, name, type_, created_at, updated_at in columns_details:
        html += f"{id_} | {name} | {type_} | {created_at} | {updated_at}<br>"
    return HttpResponse(html)


def history_operation(request):
    columns_history = History_operation.objects.values_list(
        "id", "stage_id", "work_piece_id"
    )
    html = ""
    for id_, stage_id, work_piece_id in columns_history:
        html += f"{id_} | {stage_id} | {work_piece_id}<br>"
    return HttpResponse(html)


def stages(request):
    columns_stages = Stages.objects.values_list(
        "id", "name", "created_at", "updated_at"
    )
    html = ""
    for id_, name, created_at, updated_at in columns_stages:
        html += f"{id_} | {name} | {created_at} | {updated_at}<br>"
    return HttpResponse(html)


def work_pieces(request):
    columns_work_pieces = Work_pieces.objects.values_list(
        "id", "status", "current_stage_id", "detail_id"
    )
    html = ""
    for id_, status, current_stage_id, detail_id in columns_work_pieces:
        html += f"{id_} | {status} | {current_stage_id} | {detail_id}<br>"
    return HttpResponse(html)


def index(request):
    return HttpResponse("index")
