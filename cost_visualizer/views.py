# Create your views here.
from django.shortcuts import render
from .models import CostHistory
from django.http import JsonResponse

def calculate_costs(account_count):
    # Approximate costs from ZK Compression docs
    regular_cost_sol = account_count * 0.002  # 0.2 SOL for 100 accounts
    compressed_cost_sol = account_count * 0.000004  # 0.0004 SOL for 100 accounts
    sol_price_usd = 150  # Assume 1 SOL = $150
    regular_cost_usd = regular_cost_sol * sol_price_usd
    compressed_cost_usd = compressed_cost_sol * sol_price_usd
    savings = regular_cost_usd - compressed_cost_usd
    return regular_cost_usd, compressed_cost_usd, savings

def index(request):
    history = CostHistory.objects.all()
    return render(request, 'cost_visualizer/index.html', {'history': history})

def calculate(request):
    if request.method == 'POST':
        account_count = int(request.POST.get('account_count', 100))
        regular_cost, compressed_cost, savings = calculate_costs(account_count)
        CostHistory.objects.create(
            account_count=account_count,
            regular_cost=regular_cost,
            compressed_cost=compressed_cost,
            savings=savings
        )
        return JsonResponse({
            'regular_cost': regular_cost,
            'compressed_cost': compressed_cost,
            'savings': savings
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)