/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnew.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eric <eric@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/07 18:40:20 by etexier           #+#    #+#             */
/*   Updated: 2020/01/17 17:21:14 by eric             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

char	*ft_strnew(size_t size)
{
	char	*m;

	m = (char *)malloc(size + 1);
	if (m == 0)
		return (NULL);
	ft_memset(m, 0, size + 1);
	return (m);
}
