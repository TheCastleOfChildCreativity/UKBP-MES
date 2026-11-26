from django.http import HttpResponse

from app.models import Details, History_operation, Stages, Work_pieces


def details(request):
    columns_details = Details.objects.all()
    html = ""
    for column in columns_details:
        html += f"{column.name}<br>"
    return HttpResponse(html)


def history_operation(request):
    columns_history = History_operation.objects.all()
    html = ""
    for column in columns_history:
        html += f"{column.id} | {column.stage_id} | {column.work_piece_id}<br>"
    return HttpResponse(html)


def stages(request):
    columns_stages = Stages.objects.all()
    html = ""
    for column in columns_stages:
        html += f"{column.name}<br>"
    return HttpResponse(html)


def work_pieces(request):
    columns_work_pieces = Work_pieces.objects.all()
    html = ""
    for column in columns_work_pieces:
        html += f"{column.id} | {column.status} | {column.current_stage_id} | {column.detail_id}<br>"
    return HttpResponse(html)


def index(request):
    return HttpResponse("index")
