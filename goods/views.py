from django.shortcuts import render, redirect
from . models import Good
from django.http import Http404, HttpRequest
from django.core.paginator import Paginator
from django.views.generic import ListView
from . forms import GoodsForm


def index(request, _id1=None, _id2=None, _id3=None, _id=None):

    good = Good.objects.get(pk=_id)
    name = good.name
    article = good.article
    catalog_number = good.catalog_number
    description = good.description
    in_stock = str(round(good.in_stock)) + '               ' + \
               'Наличие товара уточняйте у менеджеров. тел. 75-24-29, 75-24-30.'

    price = good.price
    if price == 0:
        price = 'Цену товара уточняйте у менеджеров. тел. 75-24-29, 75-24-30.'
    else:
        price = 'Цена:  ' + str(price * 1.2) + '  ' + 'Цену товара уточняйте у менеджеров. тел. 75-24-29, 75-24-30.'

    context = {'name': name, 'article': article, 'catalog_number': catalog_number, 'description': description,
               'in_stock': in_stock, 'price': price}

    return render(request, "goods/propeties.html", context)


class GoodsListView(ListView):
    model = Good
    template_name = "goods/goods.html"
    paginate_by = 100
    allow_empty = True
    filter = ''

    def get(self, request, *args, **kwargs):
        return super(GoodsListView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(GoodsListView, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        print(filter.__dict__)
        return Good.objects.all().filter(is_good=True).order_by("id")


def detail(request, _id):
    try:
        good = Good.objects.get(pk=_id)
    except Good.DoesNotExist:
        raise Http404("Good does not exist")
    return render(request, "goods/detail.html", {"good": good.name, "id": good.id, "description": good.description})


def good_search2(request, _id1=None, _id2=None, _id3=None, how_to_search=None, search=None):

    # обработка запроса поиска товара
    if request.method == 'GET':
        form = GoodsForm(request.GET)
        # определение наличия поиска
        if 'how_to_search' in request.GET.keys():
            how_to_search = request.GET.get('how_to_search')
            GoodsForm.how_to_search = how_to_search
        if 'search' in request.GET.keys():
            search = request.GET.get('search')
            GoodsForm.search = search
            a = search.replace(' ', '.+.')

            # вывод найденного товара
            # определение пути для правильной пагинации в найденном списке товаров
            n = request.META['QUERY_STRING'].find('&page')
            if n == -1:
                pa = '?' + request.META['QUERY_STRING'] + '&'
            else:
                pa = '?' + request.META['QUERY_STRING'][:n] + '&'

            # вывод найденных товаров без выбора категорий товаров
            if _id1 is None and _id2 is None and _id3 is None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0,
                                                                     cat3=0).order_by('name')
                if how_to_search:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, name__iregex=a).order_by('name')
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, name__iregex=a).order_by('name')
                title = "Результаты поиска в ассортименте:"
                # постраничный вывод
                paginator = Paginator(goods, 100)
                if 'page' in request.GET:
                    page_num = request.GET['page']
                else:
                    page_num = 1
                page = paginator.get_page(page_num)
                # определение контекста
                context = {'form': form, 'cat1': cat1, 'page': page, 'goods': page.object_list, 'pa': pa, 'title': title}
                return render(request, "goods/categories4.html", context)

            # вывод найденных товаров при выборе раздела 1-ого уровня
            elif _id1 is not None and _id2 is None and _id3 is None:

                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by(
                                                                     'name')
                cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                             cat3=0).order_by('name')
                if how_to_search:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, name__iregex=a).order_by('name')
                    title = "Результаты поиска в ассортименте:"
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, cat1=_id1, name__iregex=a).order_by('name')
                    cat1_name = Good.objects.get(pk=_id1).name
                    title = "Результаты поиска в категории: " + cat1_name
                # постраничный вывод
                paginator = Paginator(goods, 100)
                if 'page' in request.GET:
                    page_num = request.GET['page']
                else:
                    page_num = 1
                page = paginator.get_page(page_num)
                # определение контекста
                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'page': page, 'goods': page.object_list,
                           'pa': pa, 'title': title}
                return render(request, "goods/categories4.html", context)

            # вывод найденных товаров при выборе раздела 2-ого уровня
            elif _id1 is not None and _id2 is not None and _id3 is None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by(
                    'name')
                cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                             cat3=0).order_by(
                    'name')
                cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1,
                                                                                     cat2=_id2,
                                                                                     cat3=0).order_by('name')
                if how_to_search:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, name__iregex=a).order_by('name')
                    title = "Результаты поиска в ассортименте:"
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, cat1=_id1, cat2=_id2, name__iregex=a).order_by('name')
                    cat1_name = Good.objects.get(pk=_id1).name
                    cat2_name = Good.objects.get(pk=_id2).name
                    title = "Результаты поиска в категории: " + cat1_name + '/ ' + cat2_name
                # постраничный вывод
                paginator = Paginator(goods, 100)
                if 'page' in request.GET:
                    page_num = request.GET['page']
                else:
                    page_num = 1
                page = paginator.get_page(page_num)

                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'page': page,
                           'goods': page.object_list, 'pa': pa, 'title': title}
                return render(request, "goods/categories4.html", context)
            # вывод найденных товаров при выборе раздела 3-его уровня
            elif _id1 is not None and _id2 is not None and _id3 is not None:
                cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0, cat3=0).order_by(
                    'name')
                cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                             cat3=0).order_by(
                    'name')
                cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1,
                                                                                     cat2=_id2,
                                                                                     cat3=0).order_by('name')
                if how_to_search:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, name__iregex=a).order_by('name')
                    title = "Результаты поиска в ассортименте:"
                else:
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, cat1=_id1, cat2=_id2, cat3=_id3,
                                                                    name__iregex=a).order_by('name')
                    cat1_name = Good.objects.get(pk=_id1).name
                    cat2_name = Good.objects.get(pk=_id2).name
                    cat3_name = Good.objects.get(pk=_id3).name
                    title = "Результаты поиска в категории: " + cat1_name + '/ ' + cat2_name + '/ ' + cat3_name
                # постраничный вывод
                paginator = Paginator(goods, 100)
                if 'page' in request.GET:
                    page_num = request.GET['page']
                else:
                    page_num = 1
                page = paginator.get_page(page_num)

                context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'page': page,
                           'goods': page.object_list, 'pa': pa, 'title': title}
                return render(request, "goods/categories4.html", context)

            else:
                return redirect('catalogs')

        else:

            # определение наличия поиска
            if search is None:
                # определение пути для пагинации списка товаров
                pa = request.path + '?'

                # вывод если не выбраны категории товаров
                if _id1 is None and _id2 is None and _id3 is None and search is None:
                    cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0,
                                                                         cat3=0).order_by('name')
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True).order_by('name')
                    title = "Ассортимент товаров:"
                    # постраничный вывод
                    paginator = Paginator(goods, 100)
                    if 'page' in request.GET:
                        page_num = request.GET['page']
                    else:
                        page_num = 1
                    page = paginator.get_page(page_num)
                    context = {'form': form, 'cat1': cat1, 'page': page, 'goods': page.object_list, 'pa': pa,
                               'title': title}
                    return render(request, "goods/categories4.html", context)

                # вывод при выбранном разделе 1-ого уровня
                elif _id1 is not None and _id2 is None and _id3 is None:

                    cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0,
                                                                         cat3=0).order_by('name')
                    cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                                 cat3=0).order_by('name')
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True,
                                                                    cat1=_id1).order_by('name')
                    cat1_name = Good.objects.get(pk=_id1).name
                    title = "Товары в категории: " + cat1_name
                    # постраничный вывод
                    paginator = Paginator(goods, 100)
                    if 'page' in request.GET:
                        page_num = request.GET['page']
                    else:
                        page_num = 1
                    page = paginator.get_page(page_num)

                    context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'page': page, 'goods': page.object_list,
                               'pa': pa, 'title': title}
                    return render(request, "goods/categories4.html", context)

                # вывод при выбранном разделе 2-ого уровня
                elif _id1 is not None and _id2 is not None and _id3 is None:
                    cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0,
                                                                         cat3=0).order_by('name')
                    cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                                 cat3=0).order_by(
                        'name')
                    cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1,
                                                                                         cat2=_id2,
                                                                                         cat3=0).order_by('name')
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(
                        is_good=True, cat1=_id1, cat2=_id2).order_by('name')
                    cat1_name = Good.objects.get(pk=_id1).name
                    cat2_name = Good.objects.get(pk=_id2).name
                    title = "Товары в категории: " + cat1_name + '/ ' + cat2_name

                    # постраничный вывод
                    paginator = Paginator(goods, 100)
                    if 'page' in request.GET:
                        page_num = request.GET['page']
                    else:
                        page_num = 1
                    page = paginator.get_page(page_num)

                    context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'page': page,
                               'goods': page.object_list, "pa": pa, 'title': title}
                    return render(request, "goods/categories4.html", context)

                # вывод при выбранном разделе 3-его уровня
                elif _id1 is not None and _id2 is not None and _id3 is not None:
                    cat1 = Good.objects.values_list('id', 'name').filter(is_good=False, cat1=0, cat2=0,
                                                                         cat3=0).order_by('name')
                    cat2 = Good.objects.values_list('id', 'name', 'cat1').filter(is_good=False, cat1=_id1, cat2=0,
                                                                                 cat3=0).order_by(
                        'name')
                    cat3 = Good.objects.values_list('id', 'name', 'cat1', 'cat2').filter(is_good=False, cat1=_id1,
                                                                                         cat2=_id2,
                                                                                         cat3=0).order_by('name')
                    goods = Good.objects.values_list('id', 'name', 'article', 'catalog_number', 'cat1', 'cat2',
                                                     'cat3').filter(is_good=True, cat1=_id1, cat2=_id2,
                                                                    cat3=_id3).order_by('name')
                    cat1_name = Good.objects.get(pk=_id1).name
                    cat2_name = Good.objects.get(pk=_id2).name
                    cat3_name = Good.objects.get(pk=_id3).name
                    title = "Товары в категории: " + cat1_name + '/ ' + cat2_name + '/ ' + cat3_name
                    # постраничный вывод
                    paginator = Paginator(goods, 100)
                    if 'page' in request.GET:
                        page_num = request.GET['page']
                    else:
                        page_num = 1
                    page = paginator.get_page(page_num)

                    context = {'form': form, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'page': page,
                               'goods': page.object_list, 'pa': pa, 'title': title}
                    return render(request, "goods/categories4.html", context)

                else:
                    return redirect('catalogs')
    else:
        return redirect('catalogs')