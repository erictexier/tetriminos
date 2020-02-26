/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: etexier <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/11 17:58:02 by etexier           #+#    #+#             */
/*   Updated: 2019/11/18 14:37:18 by etexier          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

t_list	*ft_lstnew(void const *content, size_t content_size)
{
	t_list	*m;

	m = (t_list*)malloc(sizeof(t_list));
	if (m == NULL)
		return (NULL);
	m->next = NULL;
	m->content = NULL;
	m->content_size = 0;
	if (content != NULL)
	{
		m->content = (void *)malloc(content_size);
		if (m->content == NULL)
		{
			free(m);
			return (NULL);
		}
		ft_memcpy(m->content, content, content_size);
		m->content_size = content_size;
	}
	return (m);
}
