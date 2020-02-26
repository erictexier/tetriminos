/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/11 17:54:06 by etexier           #+#    #+#             */
/*   Updated: 2019/11/11 18:47:10 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

t_list	*ft_lstmap(t_list *lst, t_list *(*f)(t_list *elem))
{
	t_list	*res;
	t_list	*start;
	t_list	*last;

	start = NULL;
	while (lst)
	{
		res = f(lst);
		if (start == NULL)
			start = res;
		else
			last->next = res;
		last = res;
		lst = lst->next;
	}
	return (start);
}
