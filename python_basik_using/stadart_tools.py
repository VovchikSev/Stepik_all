# exceptions = {}
# throwed_exceptions = []
#
#
# def found_path(exceptions, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in exceptions:
#         return []
#     for node in exceptions[start]:
#         if node not in path:
#             newpath = found_path(exceptions, node, end, path)
#             if newpath: return newpath
#     return []
#
#
# n = int(input())
# for _ in range(n):
#     in_str = input().split()
#     child = in_str[0]
#     parents = in_str[2:]
#     exceptions[child] = parents
#
# m = int(input())
# for _ in range(m):
#     throwing = input()
#     for throwed_exception in throwed_exceptions:
#         if len(found_path(exceptions, throwing, throwed_exception)) > 1:
#             print(throwing)
#             break
#     throwed_exceptions.append(throwing)


# class NonPositiveError(Exception):
#     pass
#
#
# class PositiveList(list):
#     def append(self, value):
#         if value > 0:
#             super(PositiveList, self).append(value)
#         else:
#             raise NonPositiveError

# https://stepik.org/lesson/24466/step/5?unit=6773
# from datetime import date, timedelta
#
# in_date = input()
# offset = int(input())
# year, month, day = map(int, in_date.split())
# result = date(year, month, day) + timedelta(offset)
# print(result.year, result.month, result.day)


# in_str = input()
#
# if len(in_str) == 6:
#     print(in_str.upper())
# else:
#     res = in_str[:3].upper() + in_str[3:len(in_str) - 2].lower() + in_str[len(in_str) - 2:]
#     print(res)

